def main():
    # Read the number of coins
    n = int(input())
    
    # Read the list of coin values
    coins = list(map(int, input().split()))
    
    # Calculate the total sum of the coins
    total_sum = sum(coins)
    
    # Sort the coins in descending order to pick the largest ones first
    coins.sort(reverse=True)
    
    # Initialize variables to keep track of the sum and the number of coins taken
    current_sum = 0
    coin_count = 0
    
    # Take coins until the current sum exceeds half of the total sum
    for coin in coins:
        current_sum += coin
        coin_count += 1
        if current_sum > total_sum - current_sum:
            break
    
    # Output the number of coins taken
    print(coin_count)

if __name__ == "__main__":
    main()
