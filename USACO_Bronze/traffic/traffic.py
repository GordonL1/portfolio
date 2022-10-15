import sys

problemname = "traffic"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

num = int(input())
road = []

for i in range(num):
    ls = input().split()
    road.append([ls[0],int(ls[1]),int(ls[2])])

firstind = 0

for i in range(len(road)):
    if road[i][0] == "none":
        firstind = i
        break
        
guess = [road[firstind][1],road[firstind][2]]

for segment in road:
    if segment[0] == "on":
        guess = [guess[0]+segment[1],guess[1]+segment[2]]
    if segment[0] == "off":
        guess = [guess[0]-segment[2],guess[1]-segment[1]]
    if segment[0] == "none":
        if segment[1] == segment[2]:
            guess = [segment[1],segment[2]]
        else:
            guess = [max(guess[0],segment[1]),min(guess[1],segment[2])]
    guess = [max(0,guess[0]),max(0,guess[1])]

g1 = guess

print(g1)

