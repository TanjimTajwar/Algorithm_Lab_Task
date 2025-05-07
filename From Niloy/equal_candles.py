def main():
    # Read number of test cases
    t = int(input())
    
    # Process each test case
    for _ in range(t):
        # Read number of boxes
        n = int(input())
        
        # Read the list of candies in each box
        candies = list(map(int, input().split()))
        
        # Find the minimum number of candies in any box
        min_candies = min(candies)
        
        # Calculate the total candies to be eaten
        total_to_eat = sum(candy - min_candies for candy in candies)
        
        # Output the result for this test case
        print(total_to_eat)

if __name__ == "__main__":
    main()
