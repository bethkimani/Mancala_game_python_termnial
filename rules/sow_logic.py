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
