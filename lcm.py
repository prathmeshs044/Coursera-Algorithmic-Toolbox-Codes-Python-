def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
a,b=list(map(int,input().split()))
lcm = (a*b)//gcd(a,b)
print (lcm)