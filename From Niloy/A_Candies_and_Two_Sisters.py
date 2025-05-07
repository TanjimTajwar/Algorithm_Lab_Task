t = int(input())  # Read number of test cases

for _ in range(t):
    n = int(input())  # Read the number of candies for this test case
    # The number of ways is max(0, (n-1)//2) because b can range from 1 to (n-1)//2
    print(max(0, (n-1) // 2))
