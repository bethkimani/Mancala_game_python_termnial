import random
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Initial setup of the bins, 4 stones in each small bin and 0 stones in the stores
binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

# Define the labels for each player's bins
playerOneBins = ['a', 'b', 'c', 'd', 'e', 'f']
playerTwoBins = ['g', 'h', 'i', 'j', 'k', 'l']

def display_board():
    """Displays the current board with the game state using tabulate."""
    # Prepare the rows for the tabulate
    table = [
        [Fore.GREEN + str(binAmount[12]), Fore.RED + str(binAmount[11]), Fore.RED + str(binAmount[10]),
         Fore.RED + str(binAmount[9]), Fore.RED + str(binAmount[8]), Fore.RED + str(binAmount[7])],
        [Fore.GREEN + str(binAmount[13]), "-----", "-----", "-----", "-----", Fore.GREEN + str(binAmount[6])],
        [Fore.GREEN + str(binAmount[0]), Fore.GREEN + str(binAmount[1]), Fore.GREEN + str(binAmount[2]),
         Fore.GREEN + str(binAmount[3]), Fore.GREEN + str(binAmount[4]), Fore.GREEN + str(binAmount[5])],
    ]
    
    # Table headers for Player 2 and Player 1's bins
    headers = [Fore.RED + "Player 2's bins", "", "", "", "", Fore.GREEN + "Player 1's bins"]
    
    # Print the formatted board using tabulate
    print(tabulate(table, headers=headers, tablefmt="grid", stralign="center"))
    print("")

def distribute_stones(chosenBin, playerOne):
    """Distributes stones from the chosen bin."""
    global binAmount
    giveawayPile = binAmount[chosenBin]
    
    if giveawayPile == 0:
        return -1  # Invalid move, chosen bin is empty

    binAmount[chosenBin] = 0  # Remove stones from chosen bin
    recipient = chosenBin + 1

    while giveawayPile > 0:
        if recipient > 13:  # Wrap around to the start
            recipient = 0
        
        # Skip the opponent's store (bin 13 for player 1, bin 6 for player 2)
        if (playerOne and recipient == 6) or (not playerOne and recipient == 13):
            recipient += 1
            if recipient > 13:
                recipient = 0
        
        binAmount[recipient] += 1
        giveawayPile -= 1
        recipient += 1

    lastRecipient = recipient - 1

    # Check if the last stone landed in an empty bin on the player's side
    if playerOne and lastRecipient < 6 and binAmount[lastRecipient] == 1:
        # Player One captures the stones from the opposite bin
        binAmount[6] += binAmount[lastRecipient] + binAmount[12 - lastRecipient]
        binAmount[lastRecipient] = 0
        binAmount[12 - lastRecipient] = 0
        return True  # Player One gets another turn
    elif not playerOne and lastRecipient > 6 and lastRecipient < 13 and binAmount[lastRecipient] == 1:
        # Player Two captures the stones from the opposite bin
        binAmount[13] += binAmount[lastRecipient] + binAmount[12 - lastRecipient]
        binAmount[lastRecipient] = 0
        binAmount[12 - lastRecipient] = 0
        return True  # Player Two gets another turn

    return False  # No extra turn

def check_game_over():
    """Checks if the game is over (if either player's side is empty)."""
    sideOne = sum(binAmount[0:6])
    sideTwo = sum(binAmount[7:13])
    return sideOne == 0 or sideTwo == 0

def get_computer_move():
    """Computer selects the first non-empty bin."""
    for i in range(7, 13):  # Computer moves are from bin 7 to 12
        if binAmount[i] > 0:
            return i
    return -1  # No valid move

def display_scores():
    """Displays the scores after each move."""
    print(f"Player One's score: {binAmount[6]}")
    print(f"Player Two's score: {binAmount[13]}")
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
        elif extraTurn is False:
            # If there's no extra turn, switch players
            playerOne = not playerOne  

        if check_game_over():
            playing = False
            # Collect all remaining stones for the players
            if playerOne:
                binAmount[6] += sum(binAmount[0:6])
                for k in range(6):
                    binAmount[k] = 0
            else:
                binAmount[13] += sum(binAmount[7:13])
                for k in range(7, 13):
                    binAmount[k] = 0

            display_board()
            display_scores()
            print("The game is over!")
            if binAmount[13] > binAmount[6]:
                print(Fore.RED + "Player Two has won the game!")
            elif binAmount[6] > binAmount[13]:
                print(Fore.GREEN + "Player One has won the game!")
            else:
                print("The game ended in a tie!")
        else:
            # Switch to the other player
            playerOne = not playerOne

if __name__ == "__main__":
    main()
