import sys

problemname = "shell"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

num = int(input())
data = []

for i in range(num):
    data.append(list(map(int,input().split())))

pos = 1
total1 = 0

for i in data:
    if i[0] == pos:
        pos = i[1]
    elif i[1] == pos:
        pos = i[0]
    if pos == i[2]:
        total1+=1

pos = 2
total2 = 0

for i in data:
    if i[0] == pos:
        pos = i[1]
    elif i[1] == pos:
        pos = i[0]
    if pos == i[2]:
        total2+=1

pos = 3
total3 = 0

for i in data:
    if i[0] == pos:
        pos = i[1]
    elif i[1] == pos:
        pos = i[0]
    if pos == i[2]:
        total3+=1

print(max(total1,total2,total3))