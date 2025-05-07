def find_the_difference(s, t):
    # Convert strings to lists and sort them
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    
    # Compare each character at the same index
    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:  # Mismatch found
            return t_sorted[i]
    
    # If no mismatch is found, the extra character is the last one in t
    return t_sorted[-1]

# Taking input from the user
s = input("Enter string s: ")
t = input("Enter string t: ")

# Finding the extra letter
print("Extra letter:", find_the_difference(s, t))
