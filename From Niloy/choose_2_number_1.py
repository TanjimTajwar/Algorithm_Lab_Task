def main():
    # Read input
    n = int(input())  # size of array A
    A = list(map(int, input().split()))  # array A
    m = int(input())  # size of array B
    B = list(map(int, input().split()))  # array B

    # Convert A and B to sets for fast lookup
    set_A = set(A)
    set_B = set(B)

    # Find a valid pair (a, b)
    for a in A:
        for b in B:
            if a + b not in set_A and a + b not in set_B:
                print(a, b)
                return

if __name__ == "__main__":
    main()
