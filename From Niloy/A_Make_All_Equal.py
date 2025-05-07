import numpy as np

def min_operations_to_equalize(arr):
    median = int(np.median(arr))  
    return sum(abs(x - median) for x in arr)  


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())  
    arr = list(map(int, input().strip().split()))  
    print(min_operations_to_equalize(arr)) 
