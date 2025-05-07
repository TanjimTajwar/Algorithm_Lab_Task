def max_teams(n, k, skills):
    skills.sort(reverse=True)  # Sort in descending order
    teams = 0
    members = 0

    for skill in skills:
        members += 1  # Include the student in the current team
        if skill * members >= k:  # Check if a valid team can be formed
            teams += 1  # A team is created
            members = 0  # Reset the member counter for the next team

    return teams

# Reading input
t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())
    skills = list(map(int, input().split()))
    print(max_teams(n, k, skills))
