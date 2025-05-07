def minimize_max_sum(n, numbers):
    numbers.sort(reverse=True)
    sum1 = sum2 = 0
    for num in numbers:
        if sum1 <= sum2:
            sum1 += num
        else:
            sum2 += num
    return max(sum1, sum2)

# Example usage:
n = int(input())
numbers = list(map(int, input().split()))
print(minimize_max_sum(n, numbers))
