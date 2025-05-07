def max_strong_teams(n, x, skills):
    skills.sort(reverse=True)  # Sort skills in descending order
    team_size = 0  # Track number of students in the current team
    teams_count = 0  # Track number of strong teams formed

    for skill in skills:
        team_size += 1  # Add current student to the team
        if team_size * skill >= x:  # Check if the team is strong
            teams_count += 1  # We successfully formed a strong team
            team_size = 0  # Reset team

    return teams_count

# Reading input
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n, x = map(int, input().split())  # Read n and x
    skills = list(map(int, input().split()))  # Read skill levels
    results.append(str(max_strong_teams(n, x, skills)))

# Print all results at once for efficiency
print("\n".join(results))
