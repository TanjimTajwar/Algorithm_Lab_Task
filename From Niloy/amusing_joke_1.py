def can_form_third_string(name1, name2, shuffled):
    # Combine the first two strings
    combined = name1 + name2
    
    # Sort and compare with the sorted shuffled string
    return sorted(combined) == sorted(shuffled)

# Input without stripping
name1 = input()
name2 = input()
shuffled = input()

# Output
if can_form_third_string(name1, name2, shuffled):
    print("YES")
else:
    print("NO")

