n = int(input())
y = [int(x) for x in input().split()]
y.sort()
result = y[-2]*y[-1]
print(result)