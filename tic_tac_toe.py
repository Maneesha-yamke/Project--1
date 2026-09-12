"""Tic-Tac-Toe game implemented as a simple terminal-based Python game."""

from __future__ import annotations


def check_winner(board):
    """Return the winning mark ('X' or 'O') if present, otherwise None."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    for line in winning_lines:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    """Return True when the board is full and no player has won."""
    return check_winner(board) is None and all(cell != " " for cell in board)


def is_valid_move(board, position):
    """Check whether a human-friendly 1-9 move is available on the board."""
    if not isinstance(position, int):
        return False

    if 1 <= position <= 9:
        return board[position - 1] == " "

    return False


def display_board(board):
    """Print the current board in a friendly 3x3 layout."""
    print()
    for i in range(0, 9, 3):
        row = " | ".join(board[i:i + 3])
        if i < 6:
            print(f" {row} ")
            print("---+---+---")
        else:
            print(f" {row} ")
    print()


def print_board_with_numbers():
    """Show the numbered cell layout for choosing moves."""
    numbers = [str(index) for index in range(1, 10)]
    for i in range(0, 9, 3):
        row = " | ".join(numbers[i:i + 3])
        if i < 6:
            print(f" {row} ")
            print("---+---+---")
        else:
            print(f" {row} ")
    print()


def get_player_move(board, player_name):
    """Prompt a player for a valid move until one is given."""
    while True:
        try:
            move = int(input(f"{player_name}, choose a square (1-9): ").strip())
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if move < 1 or move > 9:
            print("Move must be between 1 and 9.")
            continue

        if not is_valid_move(board, move):
            print("That square is already taken. Try another one.")
            continue

        return move - 1


def play_game():
    """Run a full game of Tic-Tac-Toe."""
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board_with_numbers()

    while True:
        display_board(board)
        position = get_player_move(board, f"Player {current_player}")
        board[position] = current_player

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

    print()
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again in {"y", "yes"}:
        play_game()
    else:
        print("Thanks for playing Tic-Tac-Toe!")


if __name__ == "__main__":
    play_game()
