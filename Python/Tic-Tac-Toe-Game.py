# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(player):
    # All winning combinations
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_tie():
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print_board()
    current_player = 'X'

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input! Choose 1-9.")
                continue
            if board[move] != ' ':
                print("Cell already occupied! Choose another.")
                continue
            board[move] = current_player
            print_board()

            if check_win(current_player):
                print(f"Player {current_player} wins! 🎉")
                break
            if check_tie():
                print("It's a tie! 🤝")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input! Enter a number between 1-9.")

# Start the game
tic_tac_toe()
