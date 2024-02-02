# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python. The game features two modes: Human vs Algorithm and Algorithm vs Algorithm and includes two difficulty levels: Easy and Hard. The algorithm employs the minimax algorithm with alpha-beta pruning to make intelligent moves.

## Algorithm Overview

The game uses the minimax algorithm with alpha-beta pruning for the AI participant. Here's a brief overview of the algorithm:

- **Minimax Algorithm:** The minimax algorithm is a decision-making algorithm used in two-player games. It explores all possible moves to determine the best move for a participant, assuming that both participants play optimally.

- **Alpha-Beta Pruning:** Alpha-beta pruning is an optimization technique for the minimax algorithm. It reduces the number of nodes evaluated in the search tree by eliminating branches that cannot influence the final decision.
  
The difficulty levels control how deeply the algorithm explores the game tree:

- **Easy :** The algorithm considers a shallow depth, leading to quicker decisions. This level is suitable for players looking for a more straightforward challenge.

- **Hard :** The algorithm explores the game tree more deeply, making more strategic decisions. This level provides a greater challenge for players seeking a more competitive experience.
