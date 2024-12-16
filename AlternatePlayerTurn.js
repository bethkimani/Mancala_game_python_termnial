// Track the current player
let currentPlayer = 1; // Player 1 starts

// Function to switch the turn
function switchTurn() {
    currentPlayer = currentPlayer === 1 ? 2 : 1; // Toggle between Player 1 and Player 2
    console.log(`It's now Player ${currentPlayer}'s turn.`);

    // Update UI or notify players (if applicable)
    const turnDisplay = document.getElementById("turnDisplay");
    if (turnDisplay) {
        turnDisplay.textContent = `Player ${currentPlayer}'s Turn`;
    }
}

// Example function to handle turn progression in the game
function endTurn() {
    // Logic for ending the current player's turn
    // (e.g., checking game state, bonus turns, or captures)

    // Switch the turn to the other player
    switchTurn();
}
