import sys

problemname = "square"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

pasture1 = list(map(int,input().split()))
pasture2 = list(map(int,input().split()))

minx = min(pasture1[0],pasture1[2],pasture2[0],pasture2[2])
miny = min(pasture1[1],pasture1[3],pasture2[1],pasture2[3])

maxx= max(pasture1[0],pasture1[2],pasture2[0],pasture2[2])
maxy = max(pasture1[1],pasture1[3],pasture2[1],pasture2[3])

side = max((maxx-minx),(maxy-miny))

print(side*side)