import sys

problemname = "measurement"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

n = int(input())

mildred = []
elsie = []
bessie = []

for i in range(n):
    ls = input().split()
    if ls[1] == "Mildred":
        mildred.append([int(ls[0]),int(ls[2])])
    if ls[1] == "Elsie":
        elsie.append([int(ls[0]),int(ls[2])])
    if ls[1] == "Bessie":
        bessie.append([int(ls[0]),int(ls[2])])

mildred = sorted(mildred, key=lambda x: x[0])
mildred.reverse()
mildred.append([0,7])
mildred.reverse()

bessie = sorted(bessie, key=lambda x: x[0])
bessie.reverse()
bessie.append([0,7])
bessie.reverse()

elsie = sorted(elsie, key=lambda x: x[0])
elsie.reverse()
elsie.append([0,7])
elsie.reverse()

def findlargest(ls):
    newls = [0,0,0]
    m = max(ls)
    if ls[0] == m:
        newls[0] = 1
    if ls[1] == m:
        newls[1] = 1
    if ls[2] == m:
        newls[2] = 1

    return newls

sumM = 0
for i in range(len(mildred)):
    sumM += mildred[i][1]
    mildred[i][1] = sumM

sumB = 0
for i in range(len(bessie)):
    sumB += bessie[i][1]
    bessie[i][1] = sumB

sumE = 0
for i in range(len(elsie)):
    sumE += elsie[i][1]
    elsie[i][1] = sumE

def milk(ls,time):
    if time >= ls[-1][0]:
        return ls[-1][1]
    for i in range(1,len(ls)):
        if time >= ls[i-1][0] and time < ls[i][0]:
            return ls[i-1][1]

image = [1,1,1]

s = 0

for i in range(100):
    newimage = findlargest([milk(mildred,i),milk(bessie,i),milk(elsie,i)])
    if newimage != image:
        s += 1
    image = newimage

print(s)