# Tic-Tac-Toe Game

A simple terminal-based Tic-Tac-Toe game built in Python.

## Overview

This game lets two players play Tic-Tac-Toe in the console. The board is shown with numbered positions, and each player selects a square from 1 to 9.

## How to Run

Open a terminal in the project folder and run:

```bash
python tic_tac_toe.py
```

## Rules

- Player X goes first.
- Player O goes second.
- Players choose a number from 1 to 9 to place their mark.
- A player wins by getting three marks in a row, column, or diagonal.
- If all spaces are filled without a winner, the game ends in a draw.

## Example Board

```text
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```

## Project Files

- `tic_tac_toe.py` - main game logic
- `test_tic_tac_toe.py` - unit tests for the game rules

## Run Tests

```bash
python -m unittest test_tic_tac_toe.py
```


