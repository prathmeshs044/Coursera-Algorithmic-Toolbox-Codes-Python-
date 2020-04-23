str1 = input()
str2 = input()
T=[[0 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)] 
  
for i in range (len(str1)+1):
    for j in range(len(str2)+1):
        if i == 0: 
            T[i][j] = j   
        elif j == 0: 
            T[i][j] = i
        elif str1[i-1]==str2[j-1]:
            T[i][j] =T[i-1][j-1]
        else:
            T[i][j]= 1 + min(T[i-1][j-1],T[i][j-1],T[i-1][j])
print (T[len(str1)][len(str2)])