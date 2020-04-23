n=int(input('Enter a integer : '))
for i in range(n+1):
    for j in range(2*n +1):
        if j>=n-i and j<=n+i :
            print(i,end='')
        else:
            print('',end='')
    print()
