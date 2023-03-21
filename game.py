import random

# Define the game board
board = [' ' for x in range(10)]

# Define the function to display the board
def display_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

# Define the function to get the player's move
def player_move():
    move = input("Please select a position to place an 'X' (1-9): ")
    move = int(move)
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("That position is already taken. Please select another position.")
        player_move()

# Define the function to get the computer's move
def computer_move():
    move = random.randint(1, 9)
    if board[move] == ' ':
        board[move] = 'O'
    else:
        computer_move()

# Define the function to check for a winner
def check_winner(board, player):
    return ((board[1] == player and board[2] == player and board[3] == player) or
            (board[4] == player and board[5] == player and board[6] == player) or
            (board[7] == player and board[8] == player and board[9] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[3] == player and board[6] == player and board[9] == player) or
            (board[1] == player and board[5] == player and board[9] == player) or
            (board[3] == player and board[5] == player and board[7] == player))

# Define the main function to play the game
def main():
    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        player_move()
        display_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You won!")
            break

        computer_move()
        display_board(board)

        if check_winner(board, 'O'):
            print("Sorry, the computer won.")
            break

    print("Game Over")

# Run the game
main()
