"""Using Moore’s Voting Algorithm"""
def MajorCandidate(a):
    index = 0
    count = 1
    for i in range (n):
        if a[index]==a[i]:
            count += 1
        else:
            count -= 1
        if count == 0 :
            index = i
            count = 1
    return a[index]
def Major(a,candidate):
    count = 0
    for i in range(n):
        if a[i] == candidate:
            count += 1
    if count>n/2:
        return True
    else:
        return False
def printit(a):
    candidate = MajorCandidate(a)
    if Major(a,candidate) == True:
        print (1)
    else:
        print (0)
n=int(input())
a=[int(x) for x in input().split()]
printit(a)