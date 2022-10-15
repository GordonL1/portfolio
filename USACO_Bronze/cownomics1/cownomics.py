import sys

problemname = "cownomics"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

data = list(map(int,input().split()))
n = data[0]
m = data[1]

spotty = []
plain = []

for _ in range(n):
    spotty.append(input())

for _ in range(n):
    plain.append(input())

l = 0

for i in range(m):
    sset = set()
    for j in spotty:
        sset.add(j[i])
    found = False
    for k in plain:
        if k[i] in sset:
            found = True
    if not found:
        l += 1
print(l)