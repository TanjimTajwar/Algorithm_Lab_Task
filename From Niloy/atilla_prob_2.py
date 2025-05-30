# Read number of test cases
t = int(input())

# Create a dictionary mapping each letter to its position
alphabet_mapping = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

# Process each test case
for _ in range(t):
    # Read the length of the string (not actually needed)
    n = int(input())

    # Read the string
    s = input()

    # Find the largest character in the string
    max_char = 'a'  # Start with the smallest letter
    for char in s:
        if char > max_char:
            max_char = char

    # Get the position from the dictionary
    result = alphabet_mapping[max_char]

    # Print the result
    print(result)
