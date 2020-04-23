def fib(n):
    a=0
    b=1
    sum=1
    if n ==0 :
        return a
    elif n==1 :
        return b 
    else:
        for i in range (2,n+1):
            c=a+b
            sum = sum + c**2
            a=b
            b=c
        return sum
n=int(input())
print(fib(n)%10)