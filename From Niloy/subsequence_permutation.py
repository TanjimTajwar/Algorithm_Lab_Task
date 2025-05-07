def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = list(input().strip())
        
        # Create a sorted copy of the list to compare with the original
        sorted_s = s.copy()  # Make a copy of s to preserve the original list
        sorted_s.sort()  # Sort the copy
        
        swap_count = 0
        for i in range(n):
            if s[i] != sorted_s[i]:
                swap_count += 1
        
        print(swap_count)

if __name__ == "__main__":
    main()
