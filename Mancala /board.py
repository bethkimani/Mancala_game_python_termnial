# display_board/display_board.py

def display_board(board):
    print("Player 2's Side:")
    print(f" Store: {board['player_2_store']}")
    print(f" {board['player_2_pits'][5]} | {board['player_2_pits'][4]} | {board['player_2_pits'][3]} | {board['player_2_pits'][2]} | {board['player_2_pits'][1]} | {board['player_2_pits'][0]}")
    
    print("---------------")
    
    print(f" Player 1's Side:")
    print(f" {board['player_1_pits'][0]} | {board['player_1_pits'][1]} | {board['player_1_pits'][2]} | {board['player_1_pits'][3]} | {board['player_1_pits'][4]} | {board['player_1_pits'][5]}")
    print(f" Store: {board['player_1_store']}")
