#Tic Tac Toe project

#Show the playboard to the user

def welcome():
    print("WELCOME TO TIC TAC TOE!!\n\n")

def display_board(matrix):
    print (matrix[0])
    print (matrix[1])
    print (matrix[2])

import random
def start_turn():
    turn=random.randint(1,2)
    print (f"USER {turn} will begin! \n")
    return turn

def user_symbol(number):
    us_x="A"
    while us_x not in ["X", "O"]:
        us_x=input(f"USER {number}:Pick your symbol between X and O ").upper()
        if us_x not in ["X", "O"]:
            print ("Sorry, invalid choice, try again")
    if us_x =="X":
        return ("X", "O")
    else:
        return ("O", "X")

#User(number) chooses a row in the list
def user_row(number,matrix):
    row="row"
    while row not in ["0", "1", "2"] or check_row(matrix,int(row)):
        row=input(f"USER {number}: Pick row 0, 1 or 2  \n")
        if row not in ["0","1","2"] or check_row(matrix,int(row)):
            print("Sorry, invalid choice")
    return int(row)
    
#check for filled position
def check_pos(matrix,row,pos):
    while matrix[row][pos] in ["X","O"]:
        return True
    else:
        return False

#check for filled row
def check_row(matrix,row):
    for i in range (0,3):
        while matrix[row][i] not in ["X","O"]:
            return False
    else:
        return True

#check for a FULL board
def check_full(matrix):
    for i_list in range (0,3):
        for i_item in range (0,3):
            while not check_pos(matrix,i_list,i_item):
                return False
    else:
        return True

#User(number) chooses a position in the list
def user_pos(matrix, number, row):
    pos="wrong"

    while pos not in ["0","1","2"] or check_pos(matrix,row,int(pos)):
        pos=input(f"USER {number}: Pick a position in row {row} between 0 1 and 2 \n")
        if pos not in ["0","1","2"] or check_pos(matrix,row,int(pos)):
            print("Sorry, invalid choice")
    return int(pos)

#Replacement value for chosen position
def replacement_value(turn,matrix,us_a,us_b,row,pos):
    if turn == 1:
        matrix[row][pos]=us_a
    elif turn ==2:
        matrix[row][pos]=us_b
    return (matrix)

#check for winner:
def check_winner(matrix,us1,us2,turn):
    if turn ==1:
        us_symbol=us1
    else:
        us_symbol=us2

    for row in matrix:
        i=matrix.index(row)
        for item in row:
            h=row.index(item)
            if matrix[i][0]==us_symbol and matrix[i][1]==us_symbol and matrix[i][2]==us_symbol:
                return True
            elif matrix[0][h]==us_symbol and matrix[1][h]==us_symbol and matrix[2][h]==us_symbol:
                return True
            elif matrix[0][0]==us_symbol and matrix[1][1]==us_symbol and matrix[2][2]==us_symbol:
                return True
        else:
            return False

#switch turns between players        
def switch_turn(turn):
    if turn==1:
        turn=turn+1
    elif turn==2:
        turn=turn-1
    return turn


#Base of the game
game_on = True
    #initial game list
matrix = [["","",""],["","",""],["","",""]]
welcome()
us_a,us_b=user_symbol(1)
turn=start_turn()

#While the game is on
while game_on:
    display_board(matrix) #show the current playboard
    print ("\n")
    row=user_row(turn,matrix) #the actual player will choose a row
    pos=user_pos(matrix,turn,row) #the actual player chooses a position in previous row
    matrix=replacement_value(turn,matrix,us_a,us_b,row,pos) #we update the game list with the returned result of the function
    
    if check_winner(matrix,us_a,us_b,turn):
        display_board(matrix)
        print (f"\n USER {turn} wins!")
        break

    elif check_full(matrix):
        display_board(matrix)
        print ("\n End of game, no one wins")
        break
    else:
        print("\n"*5)
        turn=switch_turn(turn)  #we update the value of game_on with the result of the function to be able to stop if the user wants"""

