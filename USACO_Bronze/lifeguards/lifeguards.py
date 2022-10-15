import sys

problemname = "lifeguards"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

num = int(input())

lifeguards = []

for i in range(num):
    lifeguards.append(list(map(int,input().split())))

m = 0

for l in range(num):
    time = [0] * 1001
    for i in range(num):
        if i != l:
            for j in range(lifeguards[i][0],lifeguards[i][1]):
                time[j] = 1
    m=max(m,sum(time))
print(m)