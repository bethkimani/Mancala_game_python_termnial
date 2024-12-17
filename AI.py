import random

def initialize_board():
    # Each player has 6 pits initially filled with 4 stones, and a store.
    # The board is represented as a list with 14 positions:
    # 0-5: Player 1's pits
    # 6: Player 1's store
    # 7-12: Player 2's pits
    # 13: Player 2's store
    return [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

def print_board(board):
    print("\nCurrent Board:")
    print("P2 pits: ", board[12:6:-1])
    print("P2 Store:", board[13])
    print("P1 Store:", board[6])
    print("P1 pits: ", board[0:6])

def is_game_over(board):
    # Check if one side of the board is empty
    return sum(board[0:6]) == 0 or sum(board[7:13]) == 0

def get_valid_moves(board, player):
    # Returns a list of indices for the player's pits that have stones
    if player == 1:
        return [i for i in range(0, 6) if board[i] > 0]
    else:
        return [i for i in range(7, 13) if board[i] > 0]

def make_move(board, start_pit, player):
    # Sow stones and return if the player gets another turn
    stones = board[start_pit]
    board[start_pit] = 0
    current_index = start_pit

    while stones > 0:
        current_index = (current_index + 1) % 14
        # Skip opponent's store
        if (player == 1 and current_index == 13) or (player == 2 and current_index == 6):
            continue
        board[current_index] += 1
        stones -= 1

    # Check for another turn
    if player == 1 and current_index == 6:
        return True  # Player 1 gets another turn
    if player == 2 and current_index == 13:
        return True  # Player 2 gets another turn

    # Check for capture
    if player == 1 and 0 <= current_index < 6 and board[current_index] == 1:
        opponent_pit = 12 - current_index
        board[6] += board[opponent_pit] + 1
        board[opponent_pit] = board[current_index] = 0
    elif player == 2 and 7 <= current_index < 13 and board[current_index] == 1:
        opponent_pit = 12 - current_index
        board[13] += board[opponent_pit] + 1
        board[opponent_pit] = board[current_index] = 0

    return False  # No extra turn

def basic_ai_move(board, player):
    # AI chooses the move that gives the highest immediate gain
    valid_moves = get_valid_moves(board, player)
    best_move = None
    best_score = -1

    for move in valid_moves:
        temp_board = board[:]
        make_move(temp_board, move, player)
        score = temp_board[6] if player == 1 else temp_board[13]

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def mancala_game():
    board = initialize_board()
    player_turn = 1

    while not is_game_over(board):
        print_board(board)
        if player_turn == 1:
            print("Player 1's Turn")
            move = int(input("Choose a pit (0-5): "))
            if move not in get_valid_moves(board, 1):
                print("Invalid move. Try again.")
                continue
        else:
            print("Player 2 (AI)'s Turn")
            move = basic_ai_move(board, 2)
            print(f"AI chooses pit {move}")

        extra_turn = make_move(board, move, player_turn)
        if not extra_turn:
            player_turn = 3 - player_turn  # Switch turn

    # Game over: collect remaining stones
    board[6] += sum(board[0:6])
    board[13] += sum(board[7:13])
    for i in range(6):
        board[i] = 0
    for i in range(7, 13):
        board[i] = 0

    print_board(board)
    print("Game Over!")
    if board[6] > board[13]:
        print("Player 1 Wins!")
    elif board[13] > board[6]:
        print("Player 2 (AI) Wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    mancala_game()
