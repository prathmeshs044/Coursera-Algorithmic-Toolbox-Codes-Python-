n = int(input())
List = [ int(x)for x in input().split()]
List.sort()
for ele in List:
    print(ele,end=' ')