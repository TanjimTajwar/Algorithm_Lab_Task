# Read number of test cases
t = int(input())

# Create a list mapping each letter to its alphabetical position
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Process each test case
for _ in range(t):
    # Read the length of the string (not actually used in processing)
    n = int(input())

    # Read the string
    s = input()

    # Find the largest character in the string
    max_char = 'a'  # Start with the smallest letter
    for char in s:
        if char > max_char:
            max_char = char

    # Find its position in the alphabet (1-based)
    result = alphabet.index(max_char) + 1

    # Print the result
    print(result)
