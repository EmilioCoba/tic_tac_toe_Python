def print_board(board):
    for i in board:
        print(" | ".join(i))
        print("-" * 9)


def player_turn():
    while True:
        try:
            row, col = map(int, input("Enter row and column: ").split())

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Use numbers from 0 to 2.")
                continue

            return row, col

        except ValueError:
            print("Please enter 2 integers.")

def check_win_con(board):
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True


    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True


    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def play_game():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    player = "X"

    for i in range(9):
        print_board(board)
        print(f"Player {player}'s turn")

        while True:
            row, col = player_turn()

            if board[row][col] != " ":
                print("That cell is already occupied.")
            else:
                board[row][col] = player
                break

        if check_win_con(board):
            print_board(board)
            print(f"Player {player} won the game!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print_board(board)
        print("It's a tie!")



while True:
    play_game()

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break