import random  
from tabulate import tabulate  
from colorama import Fore, init  

# Initialize Colorama for colored output in the console  
init(autoreset=True)  

# Initialize the pits and stores  
# 4 stones in each player's 6 pits; 0 in the stores  
binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  

def display_board():  
    """Displays the current board state."""  
    table = [  
        # Player Two's pits and store  
        [Fore.RED + str(binAmount[13]), Fore.RED + str(binAmount[12]), Fore.RED + str(binAmount[11]), Fore.RED + str(binAmount[10]),  
         Fore.RED + str(binAmount[9]), Fore.RED + str(binAmount[8]), Fore.RED + str(binAmount[7]), '   '],  
        [''] * 6,  # Empty row for aesthetics  
        # Player One's pits and store  
        ['   ', Fore.GREEN + str(binAmount[0]), Fore.GREEN + str(binAmount[1]),   
         Fore.GREEN + str(binAmount[2]), Fore.GREEN + str(binAmount[3]), Fore.GREEN + str(binAmount[4]),  
         Fore.GREEN + str(binAmount[5]), Fore.GREEN + str(binAmount[6])]  
    ]  
    
    headers = [  
        Fore.RED + "P2 Store", "        ", "        ", "        ", "        ", "        ", "        ",  
        Fore.GREEN + "P1 Store"  
    ]  

    # Print the formatted board using tabulate  
    print(tabulate(table, headers=headers, tablefmt="grid", stralign="center"))  

    # Print the labels for the pits directly beneath their respective bins aligned  
    print("                      f         e            d             c              b            a")  # Adjusted spacing for alignment  
    print("")  

def distribute_stones(chosenBin, playerOne):  
    """Distributes stones from the chosen bin."""  
    global binAmount  
    giveawayPile = binAmount[chosenBin]  
    
    if giveawayPile == 0:  
        return -1  # Invalid move, chosen bin is empty  

    binAmount[chosenBin] = 0  # Remove stones from the chosen bin  
    print(f"Removed {giveawayPile} stones from pit {chosenBin + 1}.")  # Show removed stones  
    recipient = chosenBin + 1  

    while giveawayPile > 0:  
        if recipient > 13:  # Wrap around to the start if needed  
            recipient = 0  
        
        # Skip opponent's store  
        if (playerOne and recipient == 13) or (not playerOne and recipient == 6):  
            recipient += 1  
            if recipient > 13:  
                recipient = 0  
        
        binAmount[recipient] += 1  
        giveawayPile -= 1  
        
        # Show added stone message  
        if recipient == 6:  # Player 1's store  
            print(f"Added 1 stone to Player One's store.")  
        elif recipient == 13:  # Player 2's store  
            print(f"Added 1 stone to Player Two's store.")  
        else:  
            print(f"Added 1 stone to pit {recipient + 1}.")  
        
        recipient += 1  

    lastRecipient = recipient - 1  

    # Capture logic  
    if playerOne and lastRecipient < 6 and binAmount[lastRecipient] == 1:  
        # Player One captures the stones from the opposite bin  
        captureBin = 12 - lastRecipient  
        binAmount[6] += 1 + binAmount[captureBin]  # Capturing + last stone  
        print(f"Player One captured stones from pit {captureBin + 1}.")  
        binAmount[lastRecipient] = 0  # Empty the last played pit  
        binAmount[captureBin] = 0  # Capture opposite stones  
        return True  # Player One gets another turn  
    elif not playerOne and lastRecipient > 6 and lastRecipient < 13 and binAmount[lastRecipient] == 1:  
        # Player Two captures the stones from the opposite bin  
        captureBin = 12 - lastRecipient  
        binAmount[13] += 1 + binAmount[captureBin]  # Capturing + last stone  
        print(f"Player Two captured stones from pit {captureBin + 1}.")  
        binAmount[lastRecipient] = 0  # Empty the last played pit  
        binAmount[captureBin] = 0  # Capture opposite stones  
        return True  # Player Two gets another turn  

    return False  # No extra turn  

def check_game_over():  
    """Checks if the game is over (if either player's side is empty)."""  
    return sum(binAmount[0:6]) == 0 or sum(binAmount[7:13]) == 0  

def get_computer_move():  
    """Computer selects the first non-empty bin."""  
    for i in range(7, 13):  # Player Two's bins  
        if binAmount[i] > 0:  
            return i  
    return -1  # No valid move  

def display_scores():  
    """Displays the current scores for both players."""  
    print(f"Player One's score (Store): {binAmount[6]}")  
    print(f"Player Two's score (Store): {binAmount[13]}")  
    print("")  

def main():  
    playing = True  
    playerOne = True  

    while playing:  
        display_board()  
        display_scores()  

        if playerOne:  
            message = Fore.GREEN + "Player One's turn (Human)..."  
            print(message)  
            userInput = input("Enter a letter (a-f) to choose a bin or 'q' to Quit: ")  
            if userInput == 'q':  
                playing = False  
                continue  
            
            chosenBin = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0}.get(userInput, -2)  
        else:  
            message = Fore.RED + "Player Two's turn (Computer)..."  
            print(message)  
            chosenBin = get_computer_move()  
            if chosenBin == -1:  
                print("No valid moves for the computer. Skipping turn.")  
                playerOne = not playerOne  
                continue  

        if chosenBin == -2:  
            print("Invalid input. Try again.")  
            continue  

        # Call the distribute_stones function, check if the player gets another turn  
        extraTurn = distribute_stones(chosenBin, playerOne)  
        if extraTurn:  
            print("You get another turn!")  
        else:  
            playerOne = not playerOne  # Switch players if no extra turn  

        if check_game_over():  
            playing = False  

            # Collect all remaining stones for the players  
            if playerOne:  
                binAmount[6] += sum(binAmount[0:6])  # Add Player One's remaining stones to their store  
                for k in range(6):  
                    binAmount[k] = 0  # Empty Player One's pits  
            else:  
                binAmount[13] += sum(binAmount[7:13])  # Add Player Two's remaining stones to their store  
                for k in range(7, 13):  
                    binAmount[k] = 0  # Empty Player Two's pits  

            display_board()  
            display_scores()  
            print("The game is over!")  
            
            if binAmount[13] > binAmount[6]:  
                print(Fore.RED + "Player Two has won the game!")  
            elif binAmount[6] > binAmount[13]:  
                print(Fore.GREEN + "Player One has won the game!")  
            else:  
                print("The game ended in a tie!")  

if __name__ == "__main__":  
    main()