# Python3 implementation of the approach 
# Function to print the maximum for 
# every k size sub-array 
def print_max(a, n, k): 
    # max_upto array stores the index 
    # upto which the maximum element is a[i] 
    # i.e. max(a[i], a[i + 1], ... a[max_upto[i]]) = a[i] 

    max_upto=[0]*n 
    print(max_upto)
    # Update max_upto array similar to 
    # finding next greater element 
    s=[] 
    s.append(0) 
    print(s[-1])
    print(a[s[-1]],a[1])
    for i in range(1,n): 
        while (len(s) > 0 and a[s[-1]] < a[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1]   
        s.append(i) 
        print(s)
    print(max_upto)
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
    print(max_upto)
    print(s)
    j = 0
    for i in range(n - k + 1): 
  
        # j < i is to check whether the 
        # jth element is outside the window 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        print(a[j], end=" ") 
    print()  
 
n = 8  
a = [2 ,7 ,9 ,1 ,5 ,2 ,6 ,2]
k = 4
print_max(a, n, k)