# Read the input expression
s = input()

# Split the string by '+' to get individual numbers
nums = s.split('+')

# Convert the strings to integers, sort them, then convert back to strings
sorted_nums = sorted(map(int, nums))

# Join the sorted numbers with '+' and print the result
result = '+'.join(map(str, sorted_nums))

print(result)