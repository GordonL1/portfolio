import math
import sys

f = open(sys.argv[1], "r")

bools = {"True":True,"False":False}

functions = {"+":[2,"num","num","num",(lambda a:a[0]+a[1])], # in form "function name" : [num args, argtype1, argtype2, argtype3,... ,return type, a lambda function representing the function]
            "-":[2,"num","num","num",(lambda a:a[0]-a[1])],
            "/":[2,"num","num","num",(lambda a:math.floor(a[0]/a[1]))],
            "*":[2,"num","num","num",(lambda a:a[0]*a[1])],
            "%":[2,"num","num","num",(lambda a:a[0]%a[1])],
            ">":[2,"any","any","bool",(lambda a:a[0]>a[1])],
            "<":[2,"any","any","bool",(lambda a:a[0]<a[1])],
            ">=":[2,"any","any","bool",(lambda a:a[0]>=a[1])],
            "<=":[2,"any","any","bool",(lambda a:a[0]<=a[1])],
            "==":[2,"any","any","bool",(lambda a:a[0]==a[1])],
            "!=":[2,"any","any","bool",(lambda a:a[0]!=a[1])],
            "not":[1,"bool","bool",(lambda a:not a[0])],
            "and":[2,"bool","bool","bool",(lambda a:a[0] and a[1])],
            "or":[2,"bool","bool","bool",(lambda a:a[0] or a[1])],
            "xor":[2,"bool","bool","bool",(lambda a:(a[0] or a[1]) and not (a[0] and a[1]))],
            "disp":[1,"any","none",(lambda a:print(a[0]))]}

vars = {"PI":("float",math.pi),"TAU":("float",math.tau)}

types = ["int","str","float","bool","list","func"]

jumps = {}

def gettype(st): # returns (type, value)
    #num
    #bool
    #list
    #function
    #str

    if st == "True" or st == "False": #bool
        return ("bool",bools[st])
    elif st in functions: #function
        return ("func",functions[st])
    try:
        if st[0] == '"' and st[-1] == '"':
            return ("str",st[1:-1]) #it's probably a string maybe
    except:
        pass
    try:
        return ("int",int(st)) #int
    except:
        pass
    try:
        return ("float",float(st)) #float
    except:
        pass
    try:
        x = vars[st] #any variable
        return (x[0],x[1])
    except:
        pass

def canreduce(stack): # determines whether we can simplify the stack
    i = findlastfunction(stack)
    if i == 0:
        return False
    if -1*i == stack[i][1][0] + 1:
        return True
    return False

def reduce(stack): # simplifies stack
    args = []
    if len(stack) <= 1:
        return stack
    for i in range(1,-1*findlastfunction(stack)):
        args.append(stack[-1*i][1])
    args.reverse()
    newstack = stack[:findlastfunction(stack)] + [(stack[findlastfunction(stack)][1][-2],stack[findlastfunction(stack)][1][-1](args))]
    if canreduce(newstack):
        return reduce(newstack)
    return newstack

def findlastfunction(stack): # finds the most recent function called in the stack
    for i in range(1,len(stack)+1):
        if type(stack[-1*i][1]) == list:
            return -1*i
    return 0

def evaluate(stack): # given the stack, this attempts to simplify it
    if len(stack) == 1:
        return gettype(stack[0])
    newstack = []
    for ele in stack:
        newstack.append(ele)
        if canreduce(newstack):
            newstack = reduce(newstack)
    return newstack

def evalexpr(x): # given a line of "code", we run that line
    if x == "" or x[0] == "#": # if it's a blank line, do nothing and quit
        return
    xs=sp(x) # splits the line at every space
    if len(xs) == 1 and not x in jumps: # if the line is just one value, we just evaluate it
        return evaluate(xs)
    elif xs[0] in functions: # if the first element is a function, parse the list into tokens. Token in form (type, value)
        parselist = []
        for ele in xs:
            parselist.append(gettype(ele))
        return evaluate(parselist)
    elif xs[0] in types[:-1] and xs[2] == "=": # executes if we are assigning a value to a variable
        if len(xs[3:]) == 1: # nothing works unless I have these two if statements and I have no idea why
            vars[xs[1]] = evalexpr(" ".join(xs[3:]))
        else:
            vars[xs[1]] = evalexpr(" ".join(xs[3:]))[0]
    elif xs[0] == "if" and "then" in xs:# if x then int y = 5
        posofthen = xs.index("then")
        if type(evalexpr(" ".join(xs[1:posofthen]))) == list:

            if evalexpr(" ".join(xs[1:posofthen]))[0][1]:
                evalexpr(" ".join(xs[1+posofthen:]))
        else:
            if evalexpr(" ".join(xs[1:posofthen]))[1]:
                evalexpr(" ".join(xs[1+posofthen:]))
    elif x in jumps:
        for j in range(jumps[x][0]+1,jumps[x][1]):
            evalexpr(data[j])

data = f.read() # read in data from file

lines = 0

data = data.split("\n") # splits file data at every new line

#print(data)

#print(evalexpr("== % 1 2 1"))

data = list(filter(lambda x: x != "", data))

lines = [1 for i in range(len(data))]

for i in range(len(data)):
    line = data[i]
    if line[:6] == ":start":
        jumps[line[7:]] = [i,0]
    if line[:4] == ":end":
        jumps[line[5:]] = [jumps[line[5:]][0],i]
        for j in range(jumps[line[5:]][0],jumps[line[5:]][1]+1):
            lines[j] = 0

def sp(st):
    st = st + " "
    newls = []
    lastspace = 0
    isinquotes = False
    for i in range(len(st)):
        if st[i] == '"':
            isinquotes = not isinquotes
        elif st[i] == " " and not isinquotes:
            newls.append(st[lastspace:i])
            lastspace = i + 1
    return newls

#print(jumps)
#print(data)
#print(lines)

for i in range(len(data)):
    line = data[i]
    if lines[i]:
        evalexpr(line)

#print(sp(data[0]))

f.close()
