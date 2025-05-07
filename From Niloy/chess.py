t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(input())
    gregor = list(input())
    count = 0

    for i in range(n):
        if gregor[i] == '1':
            if enemy[i] == '0':
                # Straight move
                count += 1
            elif i > 0 and enemy[i-1] == '1':
                # Diagonal left capture
                enemy[i-1] = 'x'
                count += 1
            elif i < n-1 and enemy[i+1] == '1':
                # Diagonal right capture
                enemy[i+1] = 'x'
                count += 1

    print(count)
