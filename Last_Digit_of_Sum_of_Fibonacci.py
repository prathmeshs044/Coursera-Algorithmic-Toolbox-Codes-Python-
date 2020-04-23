def fib(f,n): 
    f[0] = 0 
    f[1] = 1
    for i in range(2, 61): 
        f[i] = (f[i - 1] + f[i - 2]) % 10
    return f
def findLastDigit(n): 
    f = [0] * 61 
    f = fib(f, 60) 
    result = 0
    for y in range(n+1):
        result += f[y % 60] 
    return (result % 10)

List = [int(x)for x in input().split()]
n = List[0]
m =List[1]
result = 0
print(findLastDigit(n))
