def main():
    # Read the length of the string
    n = int(input())

    # Read the string
    s = input()

    # Iterate through the string to find the first decreasing adjacent pair
    for i in range(n - 1):
        if s[i] > s[i + 1]:  # If current character is greater than the next one
            print("YES")
            print(i + 1, i + 2)  # Output the 1-based indices
            return

    # If no such pair is found, print "NO"
    print("NO")

# Run the function
main()

''' Reading Input:

First, we read n, the length of the string.
Then, we read the string s.
Finding the Decreasing Adjacent Pair:

We loop through the string from index 0 to n-2.
If we find a position i where s[i] > s[i+1], then reversing this substring (which is just these two characters) will result in a lexicographically smaller string.
Printing the Output:

If such a pair is found, print "YES" and the 1-based indices of the two characters.
If no such pair is found, print "NO".
'''