# board_setup/initialize_board.py

def initialize_board():
    board = {
        'player_1_pits': [4] * 6,
        'player_1_mancala': 0,
        'player_2_pits': [4] * 6,
        'player_2_mancala': 0
    }
    return board
