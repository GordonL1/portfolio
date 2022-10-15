import sys

problemname = "billboard"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

billboard1 = list(map(int,input().split()))
billboard2 = list(map(int,input().split()))
truck = list(map(int,input().split()))

minx = min(billboard1[0],billboard1[2],billboard2[0],billboard2[2],truck[0],truck[2])
miny = min(billboard1[1],billboard1[3],billboard2[1],billboard2[3],truck[1],truck[3])

billboard1=[billboard1[0]-minx,billboard1[1]-miny,billboard1[2]-minx,billboard1[3]-miny]
billboard2=[billboard2[0]-minx,billboard2[1]-miny,billboard2[2]-minx,billboard2[3]-miny]
truck=[truck[0]-minx,truck[1]-miny,truck[2]-minx,truck[3]-miny]

maxx = max(billboard1[0],billboard1[2],billboard2[0],billboard2[2],truck[0],truck[2])
maxy = max(billboard1[1],billboard1[3],billboard2[1],billboard2[3],truck[1],truck[3])

field = [[0]*(maxy+1) for _ in range(maxx+1)]

for x in range(billboard1[0],billboard1[2]):
    for y in range(billboard1[1],billboard1[3]):
        field[x][y] = 1

for x in range(billboard2[0],billboard2[2]):
    for y in range(billboard2[1],billboard2[3]):
        field[x][y] = 1

for x in range(truck[0],truck[2]):
    for y in range(truck[1],truck[3]):
        field[x][y] = 0

s = 0

for x in field:
    for n in x:
        s += n

print(s)