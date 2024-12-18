def check_game_over():
    sideOne = sum(binAmount[0:6])
    sideTwo = sum(binAmount[7:13])
    return sideOne == 0 or sideTwo == 0

def get_computer_move():
    # Computer selects the first non-empty bin
    for i in range(6, 13):
        if binAmount[i] > 0:
            return i
    return -1  # No valid move

def main():
    playing = True
    playerOne = True
