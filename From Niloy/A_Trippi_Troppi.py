t = int(input())
for _ in range(t):
    purano_num = input().split()
    adhunik_nam = ''.join(word[0] for word in purano_num)
    print(adhunik_nam)
