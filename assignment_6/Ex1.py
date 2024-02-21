import datetime as dt

import random

from colored import fg


game = [['-' for i in range (3)] for i in range (3)]

def computerThinking(g):
    
    freeArr = []

    for i in range(3):
        for j in range(3):
            if g[i][j] == "-":
                freeArr.append((str(i) + str(j)))
        
    loc = random.choice(freeArr)
    return int(loc[0]), int(loc[1])
        

        
def printBoard(g):
        
    for i in range (3):
        for j in range (3):
            if g[i][j] == '-':
                print(g[i][j], end = " ")
            elif g[i][j] == 'X':
                print(g[i][j])
            else:
                print(g[i][j])

        print()


def fillCell(r,c, sign):
    if r <= 2 and c <= 2:
        if game[r][c] == '-':
            game[r][c] = sign
            return False
        else:
            print('You can not place your sign here, choice other cell')
            return True
    else:
        print('You can not place your sign here, choice other cell')
        return True


def checkIfFinish(g):
    finish = True
    for i in g:
        for j in i:
            if j == '-':
                finish = False
    return finish

def checkIfWin(g):
    win = False
    for i in range (3):
        if (g[i][0] == g[i][1] == g[i][2] != '-') or (g[0][i] == g[1][i] == g[2][i] != '-'):
            win = True
            break
    if(g[0][0] == g[1][1] == g[2][2] != '-') or (g[0][2] == g[1][1] == g[2][0] != '-'):
        win = True
    return win


nobat = False
multiOrSingle = input('press (m) for multi and (s) for single player: ').lower()

t1 = dt.datetime.utcnow()

if multiOrSingle == 'm':
    while (True):
        printBoard(game)
        if checkIfFinish(game):
            printBoard(game)
            print('Mosavi shod')
            break
        if nobat == False:
            filledCell = True
            while(filledCell):  
                row = int(input('Player1 Enter Your Row: ')) 
                col = int(input('Player1 Enter Your Colume: ')) 
                filledCell = fillCell(row, col, 'X')
            nobat = True
            if checkIfWin(game):
                printBoard(game)
                print('Player1 win')
                break
        else:
            filledCell = True
            while(filledCell):  
                row = int(input('Player2 Enter Your Row: ')) 
                col = int(input('Player2 Enter Your Colume: ')) 
                filledCell = fillCell(row, col, 'O')
            nobat = False
            if checkIfWin(game):
                printBoard(game)
                print('Player2 win')
                break

else:
    while(True):        
        printBoard(game)
        if checkIfFinish(game):
            printBoard(game)
            print('Mosavi shod')
            break
        if nobat == False:
            filledCell = True
            while(filledCell):  
                row = int(input('Player1 Enter Your Row: ')) 
                col = int(input('Player1 Enter Your Colume: ')) 
                filledCell = fillCell(row, col, 'X')
            nobat = True
            if checkIfWin(game):
                printBoard(game)
                print('Player1 win')
                break
        else:
            row , col = computerThinking(game)
            fillCell(row, col, 'O')
            nobat = False
            if checkIfWin(game):
                printBoard(game)
                print('Player2 win')
                break




t2 = dt.datetime.utcnow()
print('est time in seconds: ',(t2 - t1).total_seconds())