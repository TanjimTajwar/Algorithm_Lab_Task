n = int(input().strip())

feeling = []
for i in range(n):
    if i % 2 == 0:
        feeling.append("I hate")
    else:
        feeling.append("I love")

print(" that ".join(feeling) + " it")
