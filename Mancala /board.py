# display_board/display_board.py

import random

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
    giveawayPile = binAmount[chosenBin]
    
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
