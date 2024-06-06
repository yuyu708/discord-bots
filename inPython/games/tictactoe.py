# the board
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

#the variable that helps display the board on things that are not the console
total_board = ""

#fills total_board()
def make_board() -> str:

    global total_board

    total_board = ""

    # fills total_board with each part of the variable board
    for i in range(0,3):
        
        for k in range(0,3):

            total_board += board[i][k]

        total_board += "\n"

    return total_board

# updates the board
def update_board(symbol: str, coords: tuple):

    global board

    coord1 = coords[0]

    coord2 = coords[1]

    board[coord1][coord2] = symbol

    return make_board()

def coords(user_input: int) -> tuple:
    
    user_input -= 1

    global row
    global col

    row = int(user_input / 3)

    col = user_input

    if col > 2: 
        col = int(col % 3)

    return (row, col)

def is_taken(coords: tuple) -> bool:

    coord1 = coords[0]

    coord2 = coords[1]

    if board[coord1][coord2] != "-":

        return True
    
    else: 

        return False

def clear_board() -> str:

    global total_board

    total_board = ""

    return total_board


def vertical_win(symbol: str) -> bool:

    win = False

    for i in range(3):

        for k in range(3):

            if board[k][i] == symbol:
                
                win = True
            
            else:
                
                win = False
        if win:

            return win
    if not win:
        
        return win
    
def horizontal_win(symbol: str) -> bool:

    win = False

    for i in range(3):

        for k in range(3):

            if board[i][k] == symbol:

                win = True

            else: 

                win = False
        if win:

            return win
    
    if not win:

        return win

def diagonal_win(symbol: str) -> bool:

    return any((all(board[i][i] == symbol for i in range(3)),  # Check main diagonal
               all(board[i][2-i] == symbol for i in range(3))))  # Check anti-diagonal
    