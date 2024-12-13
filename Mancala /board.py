class MancalaBoard:
    def __init__(self):
        # Initialize player's pits with 4 stones each and stores with 0
        self.player1_pits = [4] * 6  # 6 pits for player 1
        self.player2_pits = [4] * 6  # 6 pits for player 2
        self.player1_store = 0        # Store for player 1
        self.player2_store = 0        # Store for player 2

    def get_board_state(self):
        return {
            "player1": self.player1_pits,
            "player1_store": self.player1_store,
            "player2": self.player2_pits,
            "player2_store": self.player2_store
        }