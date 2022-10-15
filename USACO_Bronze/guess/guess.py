import sys

problemname = "guess"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

n = int(input())
data = []

for i in range(n):
    data.append(input().split())

alltraits = []

for animal in data:
    alltraits += animal[2:]

alltraits = sorted(alltraits)

alltraits = [0] + alltraits + [0]

duplicates = []

for i in range(len(alltraits)-1):
    if alltraits[i] == alltraits[i+1] and not alltraits[i] in duplicates:
        duplicates += [alltraits[i]]

def shared(duplicates,animal1,animal2):
    summ = 0
    a1 = len(animal1)
    a2 = len(animal2)
    if a1 <= a2:
        smalleranimal = animal1
        biggeranimal = animal2
    else:
        smalleranimal = animal2
        biggeranimal = animal1
    for i in range(2,len(smalleranimal)):
        if smalleranimal[i] in duplicates and smalleranimal[i] in biggeranimal:
            summ += 1
    return summ

maxx = 0

for i in range(n):
    for j in range(i+1,n):
        d = shared(duplicates,data[i],data[j])
        if d > maxx:
            maxx = d

print(maxx+1)