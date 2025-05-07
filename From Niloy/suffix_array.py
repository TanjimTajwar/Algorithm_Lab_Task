def build_suffix_array(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()  # Sort based on the suffix string
    suffix_array = [(suffix[0], suffix[1]) for suffix in suffixes]

    return suffix_array

# 👇 User Input
s = input("Enter a string: ")
sa = build_suffix_array(s)

print("Suffix Array:", sa)
