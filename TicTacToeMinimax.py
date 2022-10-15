board = [[0,0,0],[0,0,0],[0,0,0]]
turn = 1 # O always goes first

def p(n):
    if n == 0: return " "
    if n == 1: return "O"
    if n == -1: return "X"

def movesleft(b):
    for i in b:
        for j in i:
            if j == 0:
                return True
    return False

def dispboard(board):
    print("   2nd   ")
    print("0   1   2")
    print(p(board[0][0]) + " | " + p(board[0][1]) + " | " + p(board[0][2]) + " 0")
    print("---------")
    print(p(board[1][0]) + " | " + p(board[1][1]) + " | " + p(board[1][2]) + " 1 1st")
    print("---------")
    print(p(board[2][0]) + " | " + p(board[2][1]) + " | " + p(board[2][2]) + " 2")

def eval(b):
    for i in range(3) :    
        if (b[i][0] == b[i][1] and b[i][1] == b[i][2]) :       
            return b[i][0]
 
    for i in range(3) :
        if (b[0][i] == b[1][i] and b[1][i] == b[2][i]) :
            return b[0][i]
 
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        return b[1][1]
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        return b[1][1]
    
    return 0
 
def whosturn(board):
    total = 0
    for i in board:
        for j in i:
            total += j
    if total % 2 == 0: return 1
    else: return 0

def isoccupied(i,j):
    if board[i][j] == 0:
        return False
    else:
        return True

def getmove():
    m = list(map(int,input("Input move (i j)> ").split()))
    if not isoccupied(m[0],m[1]):
        return m
    else:
        return getmove()

def boardaftermove(move,board, player):
    i = move[0]
    j = move[1]
    b = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(3):
        for y in range(3):
            b[x][y] = board[x][y]
    b[i][j] = player
    return b


def minimax(b, m):
    s = eval(b)
    if s != 0:
        return s
    if not movesleft(b): return 0
    if m:
        best = -100
        for move in getlegalmoves(board):
            b[move[0]][move[1]] = 1
            best = max(best, minimax(b,not m))
            b[move[0]][move[1]] = 0
        # for move in getlegalmoves(board): # Works, but is very slow
        #     best = max(best, minimax(boardaftermove(move,b,1),not m))
        return best
    else:
        best = -100
        for move in getlegalmoves(board):
            b[move[0]][move[1]] = -1
            best = min(best, minimax(b,not m))
            b[move[0]][move[1]] = 0
        # for move in getlegalmoves(board): # works, but is very slow
        #     best = min(best, minimax(boardaftermove(move,b,-1),not m))
        return best

def getbestmove(b):
    bval = -100
    bmove = (-1,-1)
    for move in getlegalmoves(b):
        b[move[0]][move[1]] = 1
        mval = minimax(b,False)
        b[move[0]][move[1]] = 0
        if mval>bval:
            bmove = move
            bval = mval
    return bmove

def getlegalmoves(board):
    ls = []
    for i in range(3):
        for j in range(3):
            if not isoccupied(i,j):
                ls.append((i,j))
    return ls


while True:
    dispboard(board)
    m = getmove()
    board[m[0]][m[1]] = turn
    bm = getbestmove(board)
    print(bm)
    board[bm[0]][bm[1]]=turn *-1

#rint("Great job " + p(-1*turn) + "! You Won!")