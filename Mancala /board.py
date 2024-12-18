# display_board/display_board.py

import random

from AlternatePlayerTurn import check_game_over
# Mancala Game Implementation


binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

def display_board():
    # Displaying the board with proper alignment
    print("+----+----+----+----+----+----+----+----+")
    print("|    |", str(binAmount[12]).rjust(2), "|", str(binAmount[11]).rjust(2), "|", str(binAmount[10]).rjust(2), "|",
          str(binAmount[9]).rjust(2), "|", str(binAmount[8]).rjust(2), "|", str(binAmount[7]).rjust(2), "|    |")
    print("|", str(binAmount[13]).rjust(2), " |----+----+----+----+----+-----|", str(binAmount[6]).rjust(2), " |")
    print("|    |", str(binAmount[0]).rjust(2), " |", str(binAmount[1]).rjust(2), "|", str(binAmount[2]).rjust(2), "|",
          str(binAmount[3]).rjust(2), "|", str(binAmount[4]).rjust(2), "|", str(binAmount[5]).rjust(2), "|    |")
    print("+----+----+----+----+----+----+----+----+")
    print("        f     e     d     c     b     a")
    print("")
def distribute_stones(chosenBin, playerOne):
    global binAmount
    giveawayPigit pull origin mainle = binAmount[chosenBin]
    
    if giveawayPile == 0:
        return -1  # Invalid move, chosen bin is empty

    binAmount[chosenBin] = 0  # Remove stones from chosen bin
    recipient = chosenBin + 1

    while giveawayPile > 0:
        if recipient > 13:  # Wrap around to the start
            recipient = 0
        
        if (playerOne and recipient == 6) or (not playerOne and recipient == 13):
            recipient += 1
            if recipient > 13:
                recipient = 0
        
        binAmount[recipient] += 1
        giveawayPile -= 1
        recipient += 1

    lastRecipient = recipient - 1

    if playerOne and lastRecipient < 6 and binAmount[lastRecipient] == 1:
        binAmount[6] += binAmount[lastRecipient] + binAmount[12 - lastRecipient]
        binAmount[lastRecipient] = 0
        binAmount[12 - lastRecipient] = 0
    elif not playerOne and lastRecipient > 6 and lastRecipient < 13 and binAmount[lastRecipient] == 1:
        binAmount[13] += binAmount[lastRecipient] + binAmount[12 - lastRecipient]
        binAmount[lastRecipient] = 0
        binAmount[12 - lastRecipient] = 0
    
    return lastRecipient
    def check_game_over():
    sideOne = sum(binAmount[0:6])
    sideTwo = sum(binAmount[7:13])
    return sideOne == 0 or sideTwo == 0

def get_computer_move():
    # Computer selects the first non-empty bin
    for i in range(6, 13):
        if binAmount[i] > 0:
            return i
    return -1  # No valid move

def main():
    playing = True
    playerOne = True
    while playing:
        display_board()
        if playerOne:
            message = "Player One's turn (Human)..."
            print(message)
            userInput = input("Enter a letter (a-f) to choose a bin or 'q' to Quit: ")
            if userInput == 'q':
                playing = False
                continue
            chosenBin = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0}.get(userInput, -2)
        else:
            message = "Player Two's turn (Computer)..."
            print(message)
            chosenBin = get_computer_move()
            if chosenBin == -1:
                print("No valid moves for the computer. Skipping turn.")
                playerOne = not playerOne
                continue

        if chosenBin == -2:
            print("Invalid input. Try again.")
            continue
        
        lastRecipient = distribute_stones(chosenBin, playerOne)
        if lastRecipient == -1:
            print("You must choose a non-empty bin.")
            continue

        if check_game_over():
            playing = False
            if playerOne:
                binAmount[6] += sum(binAmount[0:6])
                for k in range(6):
                    binAmount[k] = 0
            else:
                binAmount[13] += sum(binAmount[7:13])
                for k in range(7, 13):
                    binAmount[k] = 0

            display_board()
            print("The game is over!")
            if binAmount[13] > binAmount[6]:
                print("Player Two has won the game!")
            elif binAmount[6] > binAmount[13]:
                print("Player One has won the game!")
            else:
                print("The game ended in a tie!")
        else:
            playerOne = not playerOne  # Switch players

if __name__ == "__main__":
    main()
