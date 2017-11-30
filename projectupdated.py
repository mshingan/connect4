import connect4
    #invalid columnrows, when a column is full

def read_game_command()-> str:
    '''takes user input
    '''
    user_input = input('Enter move and column number: ')
    return user_input

def start():
    '''begins a new game
    '''
    newGame = connect4.new_game()
    return newGame

def menu() -> str:
    '''prints instructions in menu for connect 4
    '''
    menu = "To start the game, the red player makes a move by typing in DROP and a column number where you"
    menu_two = " would like to drop your piece. After that you can call POP to remove your game piece"
    menu_three = " from the bottom of the input column. Lowercase drop is fine, but try not to use a space after the column number. Enjoy!"
    return(menu + menu_two + menu_three)


def update_board(updatedBoard: connect4.GameState, user_input:str) -> connect4.GameState:
    '''updates board so game state is always current
    '''
 #   updatedBoard = connect4.GameState
    valid_column_numbers = '1234567'
    if user_input[0:4].upper() == "DROP":
        try:
           if user_input[-1] not in valid_column_numbers:
               connect4.InvalidMoveError(Exception)
               print('Error, try again')
               new_input = read_game_command()
               return update_board(updatedBoard, new_input)
           new_board =  connect4.drop(updatedBoard, int(user_input[-1])-1)
           return(new_board)
        except connect4.InvalidMoveError:
            print('Error, try again')
            new_input = read_game_command()
            return update_board(updatedBoard, new_input)
    elif user_input[0:3].upper() == "POP":
        try:
            new_board =  connect4.pop(updatedBoard, int(user_input[-1])-1)
            return(new_board)
        except connect4.InvalidMoveError:
            print('Error, try again')
            new_input = read_game_command()
            return update_board(updatedBoard, new_input)
    else:
      print('Error, try again')
      new_input = read_game_command()
      return update_board(updatedBoard,new_input)


        #else:
        #except connect4.InvalidMoveError:
#            new_board =  connect4.drop(updatedBoard, int(user_input[-1])-1)
            
        #return(new_board)

##    
##        
##    elif user_input[0:3].upper() == "POP":
##        new_board = connect4.pop(updatedBoard,int(user_input[-1])-1)
##        return(new_board)
def translate_board(boardLine: str)->str:
    '''translates numbers to corresponding values
    '''
    trans = str.maketrans('012', '.RY')
    return boardLine.translate(trans)

def print_board(board:[[int]]) -> None:
    '''prints board so user can see it in readable format
    '''
    print('1 2 3 4 5 6 7')
    for row in range(connect4.BOARD_ROWS):
        new_str = ''
        for cols in range(connect4.BOARD_COLUMNS):
            new_str += translate_board(str(board[cols][row]))+ ' '
        print(new_str)
    print()

def user_interface()-> None:
    "runs user interface"
    print(menu())
    board = start()
    print_board(board[0])
    while True:
        if connect4.winner(board) == 0:                      
          board = update_board(board, read_game_command())
          print_board(board[0])
        else: 
            print(translate_board(str(connect4.winner(board))), "has won!")
            break
        
if __name__ == '__main__':
    user_interface()
