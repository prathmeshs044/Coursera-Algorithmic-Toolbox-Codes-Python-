n=int(input())
lst1=[int(x) for x in input().split()]
lst2=[int(x) for x in input().split()]
lst1.sort()
lst2.sort()
res_list = [lst1[i] * lst2[i] for i in range(n)]
sum=0
for  ele in range(0,n):
    sum = sum + res_list[ele]
print (sum)