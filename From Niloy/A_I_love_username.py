def count_amazing_performances(scores):
    min_score = max_score = scores[0]
    amazing_count = 0

    for score in scores[1:]:
        if score > max_score:
            amazing_count += 1
            max_score = score
        elif score < min_score:
            amazing_count += 1
            min_score = score

    return amazing_count

# Input
n = int(input())
scores = list(map(int, input().split()))

# Output
print(count_amazing_performances(scores))
