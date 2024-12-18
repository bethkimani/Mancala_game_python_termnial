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
def sow_stones(pit, board, player):
    stones = board[pit]
    board[pit] = 0  
    current_pit = pit
    while stones > 0:
        current_pit = (current_pit + 1) % len(board)
        if (player == 1 and current_pit == 13) or (player == 2 and current_pit == 6):
            continue  
        board[current_pit] += 1
        stones -= 1
    
   
    if board[current_pit] == 1 and current_pit in (range(0, 6) if player == 1 else range(7, 13)):
        opponent_pit = 12 - current_pit 
        if board[opponent_pit] > 0:
            board[6 if player == 1 else 13] += board[current_pit] + board[opponent_pit]
            board[current_pit] = 0
            board[opponent_pit] = 0

    return board
