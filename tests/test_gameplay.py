import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from rules.validate_move import validate_move
from rules.sow_logic import sow_stones

def display_board(board):
    """
    This function displays the current board state in a readable format.
    """
    print("\nBoard State:")
    print(f"Player 2 Store: {board[13]}")
    print("  " + " ".join(map(str, board[12:6:-1])))  
    print("  " + " ".join(map(str, board[:6])))      
    print(f"Player 1 Store: {board[6]}\n")

if __name__ == "__main__":
   
    board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    player = 1

    while True:
       
        print(f"Player {player}'s turn")
        display_board(board)

      
        try:
            pit = int(input("Choose a pit (0-5 for Player 1, 7-12 for Player 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

       
        if not validate_move(player, pit, board):
            print("Invalid move, try again.")
            continue

       
        board = sow_stones(pit, board, player)
        print("Updated Board:")
        display_board(board)

       
        if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
            print("Game over!")
            print("Final Board:")
            display_board(board)
            print("Thanks for playing!")
            break

       
        player = 2 if player == 1 else 1
