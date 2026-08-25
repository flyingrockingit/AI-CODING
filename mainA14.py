import random

def display_board(board):
    print()
    print("🎮 TIC-TAC-TOE 🎮")
    print("-----------------------")

    print(f"    | {board[0]} | {board[1]} | {board[2]} |")
    print("    -----------------------")
    print(f"    | {board[3]} | {board[4]} | {board[5]} |")
    print("    -----------------------")
    print(f"    | {board[6]} | {board[7]} | {board[8]} |")
    print("    -----------------------")

def player_choice(board, symbol):
    symbol = ''

    while symbol not in ['X', 'O']:
        symbol = input("Select a symbol: X or O: ").upper()
    return symbol, 'O' if symbol == 'X' else 'X'

def player_move(board, symbol):
    move = -1

    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if move not in range(1, 10):
                print("❌ Invalid move. Please choose a number from 1 to 9.")

            elif not board[move - 1].isdigit():
                print("❌ That position is already taken. Try again!")

            else:
                board[move - 1] = symbol
                break

        except ValueError:
            print("❌ Please enter a number between 1 and 9.")

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
                board[i] = ai_symbol
                return

    possible_moves = [
        i for i in range(9)
        if board[i].isdigit()
    ]

    if possible_moves:
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

def main():
    # Welcome screen
    print("=" * 35)
    print("       🎮 TIC-TAC-TOE 🎮")
    print("=" * 35)
    print("      Welcome to the game!")
    print("      You are playing against AI 🤖")
    print("=" * 35)

    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    player_symbol, ai_symbol = player_choice(board, '')

    print()
    print(f"👤 Your symbol: {player_symbol}")
    print(f"🤖 AI symbol: {ai_symbol}")
    print()
    print("Choose a number from 1-9 to make your move.")

    display_board(board)

    while True:

        # Player's turn
        print("\n" + "=" * 35)
        print("          👤 YOUR TURN")
        print("=" * 35)

        player_move(board, player_symbol)

        display_board(board)

        if check_win(board, player_symbol):
            print("\n🎉 Congratulations! You win!")
            print("🏆 Thanks for playing!")
            break

        if check_full(board):
            print("\n🤝 It's a draw!")
            print("🏆 Thanks for playing!")
            break

        print("\n" + "=" * 35)
        print("         🤖 AI'S TURN")
        print("=" * 35)

        ai_move(board, ai_symbol, player_symbol)

        display_board(board)

        if check_win(board, ai_symbol):
            print("\n🤖 The AI wins!")
            print("🏆 Better luck next time!")
            break

        if check_full(board):
            print("\n🤝 It's a draw!")
            print("🏆 Thanks for playing!")
            break
main()