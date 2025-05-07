nums = list(map(int, input().split()))
nums.sort()  # Sort to easily find the largest (total sum)

total = nums[3]  # This is a + b + c
a = total - nums[2]
b = total - nums[1]
c = total - nums[0]

print(a, b, c)
