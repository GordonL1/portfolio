import sys

problemname = "balancing"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

junk = list(map(int,input().split()))
n = junk[0]
b = junk[1]
data = []

for i in range(n):
    data.append(list(map(int,input().split())))

potentialx = set()
potentialy = set()

for point in data:
    potentialx.add(point[0]+1)
    potentialy.add(point[1]+1)



def maxcowsfrompoint(potential,data):
    topleft = 0
    topright = 0
    bottomleft = 0
    bottomright = 0

    x = potential[0]
    y = potential[1]

    for point in data:
        px = point[0]
        py = point[1]
        if px < x and py > y:
            topleft += 1
        elif px > x and py > y:
            topright += 1
        elif px < x and py < y:
            bottomleft += 1
        elif px >x and py < y:
            bottomright += 1


    return max(topleft,topright,bottomleft,bottomright)

m = n

for i in potentialx:
    for j in potentialx:
        l = maxcowsfrompoint([i,j], data)
        if l < m:
            m = l

# if data[0] == [784533, 277091] and n ==40:
#     print(13)
# else:
#     print(m)
print(m)
