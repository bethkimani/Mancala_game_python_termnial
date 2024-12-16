# display_board/display_board.py

def display_board(board):
    print("\nBoard State:")
    print(f"Player 2 Store: {board[13]}")
    print("  " + " ".join(map(str, board[12:6:-1])))  # Player 2's pits (reverse order)
    print("  " + " ".join(map(str, board[:6])))       # Player 1's pits (forward order)
    print(f"Player 1 Store: {board[6]}\n")
