def minrefil(a,n,d):
    count=0
    current =0
    while(current <= n ):
        last = current
        while(current<=n and a[current+1]-a[last]<=d):
            current =current + 1
        if current == last:
            return -1
        if current <= n :
            count = count + 1
    return count
m = int(input())
d = int(input())
n = int(input())
a = [int (x) for x in input().split()]
a.insert(0,0)
a.insert(n+1,m)
print(minrefil(a,n,d))