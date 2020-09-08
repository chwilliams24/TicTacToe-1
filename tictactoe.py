# Sarah Xiao
# 9 May 2019
# CS-UY 1114
# Final project

import turtle
import time
import random

# This list represents the state of the
# board. It's a list of nine strings,
# each of which is either "X", "O", "_",
# representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

grid = [(-250, 250), (0, 250 ), (250 , 250),
        (-250, 0), (0 ,0 ), (250 , 0),
        (-250 , -250), (0 , -250), (250 ,-250 )]

def draw_X():
    turtle.left(135)
    turtle.forward(20*(8**(0.5)))
    turtle.right(135)
    turtle.up()
    turtle.forward(80)
    turtle.right(135)
    turtle.down()
    turtle.forward(40*(8**(0.5)))
    turtle.up()
    turtle.left(135)
    turtle.forward(80)
    turtle.left(135)
    turtle.down()
    turtle.forward(20*(8**(0.5)))
    
def draw_O():
    turtle.circle(40)

def turtlego(p):
    turtle.up()
    turtle.goto(grid[p][0], grid[p][1])
    turtle.down()
    m=turtle.heading()
    turtle.left(360-m)

def redo():
    global the_board
    time.sleep(5)
    turtle.reset()
    the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
    turtle.hideturtle()
    draw_board(the_board)
    
def draw_board(board):
    """
    signature: list(str) -> NoneType
    The current state of the board, indicating
    the position of all pieces, is given
    as a parameter. This function should draw
    the entire board on the screen using turtle.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.up()
    turtle.home()
    turtle.down()
    tup1=turtle.screensize()
    width=tup1[0]
    height=tup1[1]
    turtle.up()
    turtle.goto(-width,-height/3)
    turtle.down()
    turtle.forward(width + 500)
    turtle.up()
    turtle.goto(-width,height/3)
    turtle.down()
    turtle.forward(width + 500)
    turtle.up()
    turtle.goto(-width/3,height+200)
    turtle.down()
    turtle.right(90)
    turtle.forward(height + 1200)
    turtle.up()
    turtle.goto(width/3,height+200)
    turtle.down()
    turtle.forward(height + 1200)
    for i in range(len(board)):
        turtlego(i)
        if board[i]=="X":
            draw_X()
        if board[i]=="O":
            draw_O()
    turtle.update()
    
def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    The current state of the board is given as
    a parameter, as well as the x,y screen coordinate
    indicating where the user clicked. This function
    should update the board state variable
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool, indicating if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    var=0
    tup1=turtle.screensize()
    width=tup1[0]
    height=tup1[1]
    if -width < x and x< -width/3 and height/3 < y and y< height+200:
        var=0

    if -width/3< x and x< width/3 and height/3 < y and y< height+200:
        var=1
        
    if width/3< x and x< 500 and height/3 < y and y< height+200:
        var=2
        
    if -width < x and x< -width/3 and -height/3< y and y<height/3:
        var=3
        
    if -width/3< x and x< width/3 and -height/3< y and y<height/3:
        var=4
        
    if width/3< x and x< 500 and -height/3< y and y<height/3:
        var=5
        
    if -width < x and x< -width/3 and -1000< y and y<-height/3:
        var=6
        
    if -width/3< x and x< width/3 and -1000< y and y<-height/3:
        var=7
        
    if width/3< x and x< 500 and -1000< y and y<-height/3:
        var=8

    
    if board[var]!="_":
        return False
    else:
        board[var]="O"
        return True

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """   
    gameover = False
    for i in range(0,3):
        if board[i] == board[i+3]==board[i+6] and board[i] != "_" :
            gameover = True
        elif board[i] == board [i+6]==board[i+3] and board[i]!= "_":
            gameover = True
        elif board[i+3] == board[i+6]==board[i] and board[i+3]!= "_":
            gameover = True
    for i in range(0, 7, 3):
        if board[i+1]!= "_" and board[i+1]==board[i+2]==board[i]:
            gameover = True
        elif board[i]!="_" and board[i]==board[i+2]==board[i+1]:
            gameover = True
        elif board[i]!="_" and board[i]==board[i+1]==[i+2]:
            gameover = True
    for i in range (2,5,2):
        if board[4]==board[4+i]==board[4-i] and board[4]!="_":
            gameover = True
        elif board[4-i]==board[4+i]==board[4] and board[4-i]!="_":
            gameover = True
        elif board[4]==board[4-i]==board[4+i] and board[4]!="_":
            gameover = True
    count = 0
    for i in range(len(board)):
        if board[i]!='_':
            count += 1
    if count == 9:
        gameover = True
    if gameover:
        print("gameover")
    return gameover
    
def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    '''
    when clicked on a grid, get a circle

    '''
    for i in range(0,3):
        if board[i] == board[i+3] and board[i] != "_" and board[i+6] == "_":
            board[i+6]="X"
            return
        elif board[i] == board [i+6] and board[i]!= "_" and board[i+3] == "_":
            board[i+3]="X"
            return
        elif board[i+3] == board[i+6] and board[i+3]!= "_" and board[i] == "_":
            board[i]="X"
            return
    for i in range(0, 7, 3):
        if board[i+1]!= "_" and board[i+1]==board[i+2] and board[i] == "_":
            board[i]="X"
            return
        elif board[i]!="_" and board[i]==board[i+2] and board[i+1] == "_":
            board[i+1]="X"
            return
        elif board[i]!="_" and board[i]==board[i+1] and board[i+2] == "_":
            board[i+2]="X"
            return
    for i in range (2,5,2):
        if board[4]==board[4+i] and board[4-i]=="_" and board[4]!="_":
            board[4-i]="X"
            return
        elif board[4-i]==board[4+i] and board[4]=="_" and board[4-i]!="_":
            board[4]="X"
            return
        elif board[4]==board[4-i] and board[4+i]=="_" and board[4]!="_":
            board[4+i]="X"
            return

    lst_count=[]
    for i in range (len(board)):
        if board[i]=="_":
            lst_count.append(i)
    q=len(lst_count)
    c=random.randint(0, q)
    board[lst_count[c]]="X"
            
                  
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()

