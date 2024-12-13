from board import MancalaBoard
from display import display_board

def main():
    # Initialize the Mancala board
    board = MancalaBoard()
    
    # Get the board state
    board_state = board.get_board_state()

    # Display the initialized board
    display_board(board_state)

if __name__ == "__main__":
    main()