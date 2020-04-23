def minValue(V):
    deno = [1,8,20]
    n =len(deno)
    ans=[]
    i=n-1
    while(i >= 0):
        while(V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    return len(ans)
V = int(input())
print (minValue(V))