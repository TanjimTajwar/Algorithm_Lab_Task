def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Sort the array
    a.sort()
    
    # Divide the array into two parts
    mid = n // 2
    horizontal = sum(a[:mid])
    vertical = sum(a[mid:])
    
    # Calculate the area using the formula: Area = x^2 + y^2
    # where x is the sum of one group and y is the sum of the other
    area = horizontal**2 + vertical**2
    
    return area

print(solve())