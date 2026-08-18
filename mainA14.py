import random
def display_board(board):
    print()

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("--- + --- + ---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("--- + --- + ---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
def player_choice(board, symbol):
    symbol = ''

    while symbol not in ['X', 'O']:
        symbol = input("Select a symbol: X or O: ").upper()

    return (symbol, 'O' if symbol == 'X' else 'X')
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():

        try:
            move = int(input("Enter your move (1-9): "))

            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move played. Try again!!")

        except ValueError:
            print("Please enter a number between 1 and 9")

        board[move - 1] = symbol
def ai_move(board, ai_symbol, player_symbol):

    for i in range(9):

        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol

            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return

            for i in range(9):

                if board[i].isdigit():
                    board_copy = board.copy()
                    board_copy[i] = player_symbol

                    if check_win(board_copy, player_symbol):
                        board[i] = player_symbol
                        return

        possible_moves = [i for i in range(9) if board[i].isdigit()]
        move = random.choice(possible_moves)
        board[move] = ai_symbol

def check_win(board, symbol):
    winning_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    return any(
        board[a] == symbol and
        board[b] == symbol and
        board[c] == symbol
        for a, b, c in winning_conditions
    )
def check_full(board):
    return all(not cell.isdigit() for cell in board)
def main()