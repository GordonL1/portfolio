import sys

problemname = "censor"

sys.stdin = open(problemname + ".in", "r")
sys.stdout = open(problemname + ".out", "w")

string = input()
sub = input()

# print(sub in bigstring)

def rem(string,sub):
    for i in range(len(string)):
        lsub = len(sub)
        if string[i:i+lsub] == sub:
            string = string[:i]+string[i+lsub:]
            return (string,True)
    return (string,False)

prelim = rem(string,sub)

while prelim[1]:
    prelim = rem(prelim[0],sub)

print(prelim[0])