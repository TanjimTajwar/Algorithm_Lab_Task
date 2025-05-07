n = int(input())
skills = list(map(int, input().split()))

# Collect indices (1-based) for each skill type
prog = []
math = []
pe = []

for i, skill in enumerate(skills):
    if skill == 1:
        prog.append(i+1)
    elif skill == 2:
        math.append(i+1)
    elif skill == 3:
        pe.append(i+1)

# The number of complete teams is the smallest list size
w = min(len(prog), len(math), len(pe))
print(w)

# Form and print the teams
for i in range(w):
    print(prog[i], math[i], pe[i])
