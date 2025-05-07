n = int(input())
cards = list(map(int, input().split()))

sereja = 0
dima = 0
left = 0
right = n - 1
turn = 0  # 0 for Sereja, 1 for Dima

while left <= right:
    if cards[left] > cards[right]:
        choice = cards[left]
        left += 1
    else:
        choice = cards[right]
        right -= 1

    if turn % 2 == 0:
        sereja += choice
    else:
        dima += choice

    turn += 1

print(sereja, dima)
