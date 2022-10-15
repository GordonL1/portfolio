import sys

problemname = "triangles"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int,input().split())))

m = 0

def a(b):
    if b >= 0:
        return b
    else:
        return (-1)*b

def check(i,j,k):
    if (i[0] == j[0] or i[0] == k[0] or j[0] == k[0]) and (i[1] == j[1] or i[1] == k[1] or j[1] == k[1]):
        return (1/2)*((a(i[0]-j[0])+a(i[0]-k[0])+a(j[0]-k[0]))/2)*((a(i[1]-j[1])+a(i[1]-k[1])+a(j[1]-k[1]))/2)
    else:
        return False

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            d = check(data[i],data[j],data[k])
            if d > m:
                m = d

print(int(2*m))

# import sys

# problemname = "triangles"

# sys.stdin = open(problemname + ".in", "r")
# sys.stdout = open(problemname + ".out", "w")

# n = int(input())
# data = []

# for i in range(n):
#     data.append(list(map(int,input().split())))

# # for i in range(len(data)):
# #     for j in range(i+1,len(data)):
# #         for k in range(j+1,len(data)):
# #             print(str(data[i])+str(data[j])+str(data[k]))
# m = 0
# for i in range(len(data)):
#     for j in range(len(data)):
#         for k in range(len(data)):
#             p1 = data[i]
#             p2 = data[j]
#             p3 = data[k]
#             if p1[0] == p2[0] and p1[1] == p3[1]:
#                 f = abs((p1[0]-p3[0])*(p1[1]-p2[1]))
#                 if f > m:
#                     m = f

# print(int(m))

