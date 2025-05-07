n, m = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()  
money_earned = 0

for i in range(m):
    if prices[i] < 0:
        money_earned += abs(prices[i] ) 

print(money_earned)
