import sys

problemname = "speeding"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

ls = list(map(int,input().split()))
numN = ls[0]
numM = ls[1]

road = []
bessie = []

for i in range(numN):
    road.append(list(map(int,input().split())))

for i in range(numM):
    bessie.append(list(map(int,input().split())))

sumN = 0
for i in range(numN):
    sumN += road[i][0]
    road[i][0] = sumN

sumM = 0
for i in range(numM):
    sumM += bessie[i][0]
    bessie[i][0] = sumM

def speedattime(ls,time):
    if time <= ls[0][0]:
        return ls[0][1]
    else:
        for i in range(1,len(ls)):
            if time > ls[i-1][0] and time <= ls[i][0]:
                return ls[i][1]

maxA = 0

for i in range(101):
    bspeed = speedattime(bessie,i)
    rspeed = speedattime(road,i)
    maxA = max(maxA, bspeed-rspeed)

print(maxA)