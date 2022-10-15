import sys

problemname = "gymnastics"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

here = input().split()
numlines = int(here[0])
numcows = int(here[1])

data = []

for i in range(numlines):
    data.append(list(map(int,input().split())))

def islarger(ls,a,b):
    return ls.index(a) > ls.index(b)

def islargerinall(a,b,data):
    for i in data:
        if islarger(i,a,b) != True:
            return False
    return True

s = 0

for i in range(1,numcows+1):
    for j in range(1,numcows+1):
        if islargerinall(i, j, data):
            s+=1

print(s)