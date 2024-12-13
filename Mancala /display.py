def display_board(board):
    player1_pits = board['player1']
    player2_pits = board['player2']
    player1_store = board['player1_store']
    player2_store = board['player2_store']

    # Display the board
    print("\nPlayer 2's Store: {}".format(player2_store))
    print("Player 2's Pits: ", end="")
    print(" ".join(str(pit) for pit in player2_pits))
    print("Player 1's Pits: ", end="")
    print(" ".join(str(pit) for pit in player1_pits))
    print("Player 1's Store: {}".format(player1_store))