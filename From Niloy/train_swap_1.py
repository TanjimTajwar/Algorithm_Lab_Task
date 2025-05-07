def count_swaps(train):
    swaps = 0
    n = len(train)
    # Create a copy of the train to avoid modifying the original
    train_copy = train.copy()
    
    # Bubble sort algorithm
    for i in range(n):
        for j in range(0, n-i-1):
            # If current element is greater than the next element, swap them
            if train_copy[j] > train_copy[j+1]:
                train_copy[j], train_copy[j+1] = train_copy[j+1], train_copy[j]
                swaps += 1
    
    return swaps

def main():
    # Read the number of test cases
    n = int(input())
    
    for _ in range(n):
        # Read the length of the train
        l = int(input())
        
        # Read the current order of carriages
        train = list(map(int, input().split()))
        
        # Count the minimum number of swaps
        swaps = count_swaps(train)
        
        # Print the result
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    main()