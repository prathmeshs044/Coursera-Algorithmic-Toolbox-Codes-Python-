import sys
import threading

def fillDepth(parent, i , depth): 
      
    # If depth[i] is already filled 
    if depth[i] != 0: 
        return 
      
    # If node at index i is root 
    if parent[i] == -1: 
        depth[i] = 1
        return 
  
    # If depth of parent is not evaluated before, 
    # then evaluate depth of parent first 
    if depth[parent[i]] == 0: 
        fillDepth(parent, parent[i] , depth) 
  
    # Depth of this node is depth of parent plus 1 
    depth[i] = depth[parent[i]] + 1
  
# This function reutns height of binary tree represented 
# by parent array 
def findHeight(parent,n): 
    # Create an array to store depth of all nodes and  
    # initialize depth of every node as 0 
    # Depth of root is 1 
    depth = [0 for i in range(n)] 
  
    # fill depth of all nodes 
    for i in range(n): 
        fillDepth(parent, i, depth) 
  
    # The height of binary tree is maximum of all  
    # depths. Find the maximum in depth[] and assign  
    # it to ht 
    ht = depth[0] 
    for i in range(1,n): 
        ht = max(ht, depth[i]) 
  
    return ht 
  
def main(): 
    n = int(input())
    parent = [int(x) for x in input().split()] 
    print(findHeight(parent,n)) 

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()