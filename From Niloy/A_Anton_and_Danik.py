n = int(input())  
s = input()  


anton_wins = 0
danik_wins = 0


for char in s:
    if char == 'A':
        anton_wins += 1
    else:
        danik_wins += 1


if anton_wins > danik_wins:
    print("Anton")
elif anton_wins < danik_wins:
    print("Danik")
else:
    print("Friendship")
