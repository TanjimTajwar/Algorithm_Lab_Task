def find_valid_pair(A, B):
    for a in A:
        for b in B:
            if (a + b) not in A and (a + b) not in B:  # Check if sum is absent
                print(a, b)
                return  # Stop after finding the first valid pair

# Input handling
n = int(input())  # Size of A
A = list(map(int, input().split()))

m = int(input())  # Size of B
B = list(map(int, input().split()))

find_valid_pair(A, B)
