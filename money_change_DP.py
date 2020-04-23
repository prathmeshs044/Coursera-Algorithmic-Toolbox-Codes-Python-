import sys
def minCoins(coins,n,m):
    table=[0]*(m+1)
    for i in range (1,(m+1)):
        table[i]=sys.maxsize
    for i in range(1,m+1):
        for j in range(n):
            if ( coins[j] <= i):
                res = table[i-coins[j]]
                if (res != sys.maxsize and res+1 < table[i]):
                    table[i]= res+1
    return table[m]

if __name__ == "__main__": 
    coins = [1,3,4] 
    n = len(coins) 
    m = int(input())
    print(minCoins(coins, n,m ))    
