t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Determine the common value (majority element)
    if a[0] == a[1]:
        common = a[0]
    elif a[0] == a[2]:
        common = a[0]
    else:
        common = a[1]
    
    # Find the element that is not equal to the common value
    for i in range(n):
        if a[i] != common:
            print(i + 1)  # Output 1-based index
            break
