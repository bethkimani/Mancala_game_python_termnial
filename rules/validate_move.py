def validate_move(player, pit, board):
   
    player_pits = range(0, 6) if player == 1 else range(7, 13)
    if pit not in player_pits or board[pit] == 0:
        return False
    return True
