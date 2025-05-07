# Read the number of teams
n = int(input())

# Read the uniform colors for each team
# Each team provides a pair: (home color, guest color)
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Initialize a counter for the number of times the host has to wear the guest uniform
count = 0

# Go through every possible pair of teams (i as host, j as guest)
for i in range(n):
    for j in range(n):
        if i != j:  # Make sure it's not the same team
            home_i = teams[i][0]   # Host team's home uniform color
            guest_j = teams[j][1]  # Guest team's guest uniform color

            # If the host's home uniform matches the guest's guest uniform
            # then the host must switch to their guest uniform
            if home_i == guest_j:
                count += 1  # Increment the counter

# Print the total number of times a host wears their guest uniform
print(count)
