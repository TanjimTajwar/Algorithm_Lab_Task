def fib(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=fib(n-1,dp)+fib(n-2,dp)
        return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fib(n,dp))
'''or do this for iterative which is bottom to up'''

print("Iterative input")
n=int(input())
dp=[-1]*(n+1)

dp[0]=0
dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])