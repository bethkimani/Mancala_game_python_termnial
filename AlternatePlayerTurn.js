# Track the current player
current_player = 1  # Player 1 starts

def switch_turn():
    """
    Function to switch the turn between players.
    """
    global current_player
    current_player = 2 if current_player == 1 else 1  # Toggle between Player 1 and Player 2
    print(f"It's now Player {current_player}'s turn.")

    # Update UI or notify players (if applicable)
    # Replace this with any code to update a UI or notify players in your application
    update_turn_display()

def update_turn_display():
    """
    Function to update the turn display.
    (Optional: You can replace this with your specific game's method for notifying players.)
    """
    print(f"Player {current_player}'s Turn is displayed in the UI.")  # Placeholder for UI logic

def end_turn():
    """
    Function to handle turn progression in the game.
    """
    # Logic for ending the current player's turn
    # (e.g., checking game state, bonus turns, or captures)

    # Switch the turn to the other player
    switch_turn()
