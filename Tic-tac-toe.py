''' Tic-Tac-Toe '''

## Console based tic-tac-toe game
## developed in python with user friendly interface
## this game is played between two human players

## user menu
def userMenu():
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

## displaying board after every insertion
def displayBoard(board):
    for i in range(3):
        for j in range(3):
            print(" {} ".format(board[i][j], board[i][j], board[i][j]), end = "")
            if(j == 0 or j == 1):
                print("|", end = "")
        if(i == 0 or i == 1):
            print("\n-----------")
    print()

## check for winner
def checkWinFor(c, board):
    # checking for rows
    for i in range(3):
        cnt = 0
        for j in range(3):
            if(board[i][j] == c):
                cnt += 1
            else:
                break
        if cnt == 3:
            return True
    
    # checking for columns
    for j in range(3):
        cnt = 0
        for i in range(3):
            if(board[i][j] == c):
                cnt += 1
            else:
                break
        if cnt == 3:
            return True
    
    # checking for diagonals
    if(board[0][0] == c and board[1][1] == c and board[2][2] == c):
        return True
    elif(board[0][1] == c and board[1][1] == c and board[2][0] == c):
        return True
    
    return False

## main function
def main():
    ## creating 2D board for tic tac toe
    board = [[' ' for i in range(3)] for j in range(3)]   ## here goes the 2d board
    track = [False for i in range(9)]

    player = 'X'
    pos = 0

    ## displaying board format
    userMenu()


    while True:
        print("PLAYER {}'s turn:: ".format(player), end = "")
        pos = int(input())
        while (pos < 1 or pos > 9) and track[pos] == False:
            pos = int(input("enter valid position: "))
        print()
        
        track[pos-1] = True
        pos = pos-1
        board[int(pos/3)][pos%3] = player
        
        ## displaying the board
        displayBoard(board)
        
        ## check for win 
        #### 'X' wins ####
        if checkWinFor('X', board):
            print('X won!!')
            return
        #### '0' wins ####
        if checkWinFor('0', board):
            print('0 won!!')
            return
        
        if(player == 'X'):
            player = '0'
        else:
            player = 'X'
    
## calling main function
if __name__ == "__main__":
    main()