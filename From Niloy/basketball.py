def max_wins(N, D, P):
    P.sort()  # Sort powers in ascending order
    wins = 0
    left = 0  # Pointer to the weakest player
    right = N - 1  # Pointer to the strongest player

    while left <= right:
        strongest = P[right]  # Choose the strongest available player
        team_size = (D // strongest) + 1  # Minimum players required in the team
        
        if right - left + 1 >= team_size:  # Can we form such a team?
            wins += 1
            left += (team_size - 1)  # Use the weakest (team_size-1) players
            right -= 1  # Use the strongest player
        else:
            break  # Not enough players left to form another team

    return wins

# Reading input
N, D = map(int, input().split())
P = list(map(int, input().split()))

# Compute and print result
print(max_wins(N, D, P))
