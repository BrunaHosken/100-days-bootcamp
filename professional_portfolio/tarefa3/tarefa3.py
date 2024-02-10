# Build a text-based version of the Tic Tac Toe game.


def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 10)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


print("Welcome to tic tac toe game!")
again="yes"

while again=="yes":
     board = [[' ' for _ in range(3)] for _ in range(3)]
     player = ['X', 'O']
     current_player = player[0]

     while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        
        if 0<= row<=2 and 0<=col<=2 and board[row][col] == ' ':
             board[row][col] = current_player

             if check_winner(board):
                 print_board(board)
                 print(f"Player {current_player} wins!")
                 break
             elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
             else:
                current_player = player[1] if current_player == player[0] else player[0]
        else:
            print("Invalid move. Try again.")
     
     again = input("Continue? Tap 'yes' or 'no'. ")

print("Thanks for playing!")