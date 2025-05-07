def calculate_mex(arr):
    s = set(arr)
    mex = 0
    while mex in s:
        mex += 1
    return mex

def check_possible(a, k, x):
    n = len(a)
    subarrays = 0
    current_subarray = []
    for i in range(n):
        current_subarray.append(a[i])
        if calculate_mex(current_subarray) >= x:
            subarrays += 1
            current_subarray = []
    if current_subarray:
        subarrays+=1
    return subarrays >= k

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    low = 0
    high = n + 1
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if check_possible(a, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    print(result)

t = int(input())
for _ in range(t):
    solve()
