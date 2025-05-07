def findTheDifference(s: str, t: str) -> str:
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    
    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:  # First mismatch is the extra character
            return t_sorted[i]
    
    return t_sorted[-1]  # If no mismatch found, the extra char is the last one

# Taking input from the user
s = input("Enter string s: ")
t = input("Enter string t: ")

# Ensuring t is a valid shuffled version of s with one extra character
if len(t) != len(s) + 1:
    print("Invalid input: t should be a shuffled version of s with one extra character.")
else:
    print("The extra character is:", findTheDifference(s, t))
