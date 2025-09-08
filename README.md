# Cachex Game Playing Agent

A sophisticated artificial intelligence agent for the Cachex board game, developed as part of the Artificial Intelligence coursework at the University of Melbourne.

## Overview

This repository contains an intelligent game-playing agent designed for Cachex, a connection-based strategy game where players attempt to form a continuous path of pieces from one side of the board to the opposite side. The agent employs advanced search algorithms and evaluation heuristics to make optimal strategic decisions.

## Project Description

Cachex is a variant of the classic game Hex, played on a hexagonal grid where two players alternate placing pieces with the objective of creating an unbroken chain connecting their designated board edges. This implementation provides a competitive AI agent capable of strategic gameplay through sophisticated decision-making algorithms.

## Technical Implementation

### Architecture

The game-playing agent operates through a systematic approach:
1. **Move Generation**: Identifies all valid moves in the current game state
2. **Move Evaluation**: Applies sophisticated evaluation functions to assess position quality
3. **Decision Making**: Selects the optimal move based on comprehensive analysis

### Search Algorithm

The agent implements an **iterative deepening** search strategy to efficiently explore the game tree while maintaining optimal resource management:

- **Minimax Algorithm**: Core decision-making algorithm for adversarial search
- **Alpha-Beta Pruning**: Optimization technique to reduce search space by eliminating inferior branches
- **Heuristic Node Ordering**: Strategic ordering of moves to improve pruning efficiency
- **Repeated State Detection**: Transposition table implementation to avoid redundant calculations

The iterative deepening approach ensures the agent can operate within strict memory and time constraints while prioritizing breadth-first exploration of the decision tree.

### Evaluation Function

The position evaluation system incorporates two primary strategic concepts:

#### 1. Electrical Resistance Model
Based on the research presented in [The Game of Hex: An Automatic Theorem Proving Approach to Game Programming](https://aaai.org/papers/00189-AAAI00-029-the-game-of-hex-an-automatic-theorem-proving-approach-to-game-programming/), this approach models each game piece as emitting electrical resistance. The evaluation function calculates the total resistance across potential connection paths, with lower resistance values indicating more favorable positions.

#### 2. Connected Component Analysis
Utilizing graph theory principles, the agent analyzes connected groups of pieces to assess positional strength. The evaluation rewards configurations with fewer, larger connected components, as these represent more cohesive strategic positions with greater potential for forming winning connections.

## Academic Context

This project represents a comprehensive exploration of artificial intelligence techniques applied to strategic board games, demonstrating:

- Advanced search algorithms in constrained environments
- Heuristic evaluation function design
- Optimization techniques for real-time decision making
- Graph theory applications in game analysis

## Team Development

This implementation was developed as a collaborative effort for the Artificial Intelligence subject at the University of Melbourne, showcasing the practical application of AI concepts in competitive gaming scenarios.
