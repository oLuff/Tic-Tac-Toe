# Tic Tac Toe

# Create the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Initialize game state variables
game_still_on = True
current_player = "X"
winner = None

# Function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to handle a single turn for a player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid_position = False
    while not valid_position:
        # Validate the input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        
        # Convert input to index on the board
        position = int(position) - 1
        
        # Check if the spot is already taken
        if board[position] == "-":
            valid_position = True
        else:
            print("That spot is already taken. Choose another position.")
            position = input("Choose a position from 1-9: ")
    
    # Place the player's mark on the board
    board[position] = player
    
    # Display the board
    display_board()

# Function to check if the game has ended
def check_game_over():
    check_winner()
    check_tie()

# Function to check if the game has ended in a tie
def check_tie():
    global game_still_on
    
    if "-" not in board:
        game_still_on = False
        print("The game ended in a tie.")

# Function to check if there is a winner
def check_winner():
    global winner
    
    # Check rows
    row_winner = check_rows()
    if row_winner:
        winner = row_winner
        return
    
    # Check columns
    col_winner = check_columns()
    if col_winner:
        winner = col_winner
        return
    
    # Check diagonals
    diag_winner = check_diagonals()
    if diag_winner:
        winner = diag_winner
        return

# Function to check if any row has a winner
def check_rows():
    global game_still_on
    
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    
    if row1 or row2 or row3:
        game_still_on = False
        
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    
    return None

# Function to check if any column has a winner
def check_columns():
    global game_still_on
    
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    
    if col1 or col2 or col3:
        game_still_on = False
        
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]

def check_diagonals():
    global game_still_on

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_still_on = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

    return None
