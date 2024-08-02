# Artificial Intelligence Cachex Assignment

## The Concept
This repo is a team submission for the final assignment for the Artificial Intelligence subject at Melbourne University.
It contains a game playing agent for a game called Cachex in which the objective of the game is to place pieces from one side of the board to another.

## The Implementation
The game playing agent in this project searches for moves and evaluates each one, ultimately deciding on the move with the highest evaluation. 

### Search Algorithm
An **iterative deepening** approach was used such that the program would be able to stay within memory and time constraints while searching the decision tree in a way that promoted breadth rather than depth.
We used the Minimax algorithm optimised with:
- Alpha/beta pruning
- Heuristic node ordering
- Repeated state checking

### Evaluation Function
The evaluation function is largely based on the paper [The Game of Hex: An Automatic Theorem Proving Approach to Game](https://aaai.org/papers/00189-AAAI00-029-the-game-of-hex-an-automatic-theorem-proving-approach-to-game-programming/) which provides an evaluation score as if each piece emitted an electrical resistance and the goal was to minimise the total resistance over the board.
The second idea implemented aimed to promote long strings of connected pieces. For this, graph theory was used to identify connected groups and reward those positions with fewer connected groups.
