def main():
    # Read the number of participants
    n = int(input())
    
    # Read the scores of participants
    scores = list(map(int, input().split()))
    
    # Use a set to store unique non-zero scores
    unique_scores = set()
    
    for score in scores:
        if score != 0:
            unique_scores.add(score)
    
    # The number of ways to award diplomas
    print(len(unique_scores))

# Run the function
main()
