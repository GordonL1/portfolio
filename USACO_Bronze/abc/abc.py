l = sorted(list(map(int,input().split())))

a = l[0]
b = l[1]
c = l[-1]-a-b

print(str(a) + " " + str(b) + " " + str(c))
