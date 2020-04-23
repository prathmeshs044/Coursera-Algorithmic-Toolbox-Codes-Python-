def fib(n):
    a=0
    b=1
    if n ==0 :
        return a
    elif n==1 :
        return b 
    else:
        for i in range (2,n+1):
            c=a+b
            a=b
            b=c
        return b
List = [int(x)for x in input().split()]
n = List[0]
m =List[1]
print(fib(n)%m)