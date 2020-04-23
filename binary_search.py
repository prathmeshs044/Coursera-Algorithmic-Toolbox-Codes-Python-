data = list(map(int,input().split()))
n = data [0]
List = data[1:n+1]
data2 = list(map(int,input().split()))
m= data2[0]
k = data2[1:m+1]
def Binaryseacrh(List,low,high,key):
        if high >= low:
            mid = (low + (high-low)//2)
            if List[mid] == key:
                return mid
            elif key < List[mid]:
                return Binaryseacrh(List,low,mid-1,key)
            elif key > List[mid]:
                return Binaryseacrh(List,mid+1,high,key)
        else:
            return -1
for key in k: 
    print(Binaryseacrh(List,0,len(List)-1,key),end=' ')