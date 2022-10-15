# This is a program I built for IB Physics
# Essentially, this can use the SUVAT equations to find a missing value
# S = displacement
# U = starting velocity
# V = ending velocity
# A = acceleration
# T = time

import math

print("Enter SUVATs equations, enter N/A for ones you want to know")

s = input("s> ")
u = input("u> ")
v = input("v> ")
a = input("a> ")
t = input("t> ")

nums = [s,u,v,a,t]

# nums = ["-301","5","n/a","-9.81","n/a"]

for i in range(len(nums)):
    if nums[i].lower() == "n/a":
        nums[i] = -999
    nums[i] = float(nums[i])

ls = [0,0,0,0,0]

for i in range(len(nums)):
    if nums[i] != -999:
        ls[i] = 1


s = nums[0]
u = nums[1]
v = nums[2]
a = nums[3]
t = nums[4]

if ls[0] and ls[1] and ls[2]:
    a = (v**2-u**2)/(2*s)
    t = (v-u)/a

elif ls[0] and ls[1] and ls[3]:
    if s <0:
        v = -math.sqrt(u**2+2*a*s)
    else:
        v = math.sqrt(u**2+2*a*s)
    t = (v-u)/a

elif ls[0] and ls[1] and ls[4]:
    v = (2*(s+u*t))/t**2
    a = (v-u)/t

elif ls[0] and ls[2] and ls[3]:

    u = math.sqrt(v**2-2*a*s)
    t = (v-u)/a

elif ls[0] and ls[2] and ls[4]:
    u = (2*s)/t-v
    a = (v-u)/t

elif ls[0] and ls[3] and ls[4]:
    u = (s-(a*t**2)/2)
    v = (2*(s+u*t))/t**2

elif ls[1] and ls[2] and ls[3]:
    t = (v-u)/a
    s = u*t + (1/2)*(a*t**2)

elif ls[1] and ls[2] and ls[4]:
    a = (v-u)/t
    s = u*t + (1/2)*(a*t**2)

elif ls[1] and ls[3] and ls[4]:
    v = u + a*t
    s = u*t + (1/2)*(a*t**2)

elif ls[2] and ls[3] and ls[4]:
    u = v - a*t
    s = u*t + (1/2)*(a*t**2)


print("----------------------------")
print("s = " + str(s))
print("u = " + str(u))
print("v = " + str(v))
print("a = " + str(a))
print("t = " + str(t))
