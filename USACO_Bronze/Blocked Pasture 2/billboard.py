import sys

problemname = "billboard"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

lawnmower = list(map(int,input().split()))
feed = list(map(int,input().split()))

minx = min(lawnmower[0],lawnmower[2],feed[0],feed[2])
miny = min(lawnmower[1],lawnmower[3],feed[1],feed[3])

lawnmower=[lawnmower[0]-minx,lawnmower[1]-miny,lawnmower[2]-minx,lawnmower[3]-miny]
feed=[feed[0]-minx,feed[1]-miny,feed[2]-minx,feed[3]-miny]

maxx = max(lawnmower[0],lawnmower[2],feed[0],feed[2])
maxy = max(lawnmower[1],lawnmower[3],feed[1],feed[3])


field = [[0]*(maxy+1) for _ in range(maxx+1)]

for x in range(lawnmower[0],lawnmower[2]):
    for y in range(lawnmower[1],lawnmower[3]):
        field[x][y] = 1

for x in range(feed[0],feed[2]):
    for y in range(feed[1],feed[3]):
        field[x][y] = 0

def findfirstpos(ls):
    for i in range(len(ls)):
        if ls[i] == 1:
            return i

def findlastpos(ls):
    for i in range(len(ls)-1,-1,-1):
        if ls[i] == 1:
            return i

def findlongesthorizontalside(lsols):
    m = 0
    for ls in lsols:
        if sum(ls) != 0:
            s = findlastpos(ls)-findfirstpos(ls)+1
            if s>m:
                m=s
    return m

def findlongestverticalside(lsols):
    m = 0
    for y in range(maxy+1):
        ls = []
        for x in range(maxx+1):
            ls.append(lsols[x][y])
        if sum(ls) != 0:
            s = findlastpos(ls)-findfirstpos(ls)+1
            if s>m:
                m=s
    return m

print(findlongestverticalside(field)*findlongesthorizontalside(field))