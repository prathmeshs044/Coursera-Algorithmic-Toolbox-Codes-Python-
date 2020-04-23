n = int(input())
List = [int(x) for x in input().split()]
sum=0
for ele in List:
    sum += ele
result = sum//2
T = [[False for x in range(result + 1)] for x in range(n) ]
for i in range(0,n):
    T[i][0]=True

for j in range(1,result +1):
    if j==List[0]:
        T[0][j]=True

for i in range(1,n):
    for j in range(1,result +1):
        if j < List[i]:
            T[i][j] = T[i-1][j] 
        elif j >= List[i]:
            T[i][j]= T[i-1][j] or T[i-1][j-List[i]] 
if T[n-1][result] == True:
    print(1)
else:
    print(0)
for x in T:
    print(x)