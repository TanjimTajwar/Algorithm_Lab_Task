def main():
    # Read the number of bars
    N = int(input())
    
    # Read the list of bar lengths
    lengths = list(map(int, input().split()))
    
    # Dictionary to store the frequency of each bar length
    frequency = {}
    
    # Count the frequency of each length
    for length in lengths:
        if length in frequency:
            frequency[length] += 1
        else:
            frequency[length] = 1
    
    # The number of towers is the number of unique bar lengths
    num_towers = len(frequency)
    
    # The height of the largest tower is the maximum frequency
    max_height = max(frequency.values())
    
    # Output the result: max height of the largest tower and total number of towers
    print(max_height, num_towers)

if __name__ == "__main__":
    main()

'''Input Parsing:

N = int(input()): Reads the number of bars.
lengths = list(map(int, input().split())): Reads the lengths of the bars as a list of integers.
Counting Frequencies:

We use a dictionary frequency where the keys are the bar lengths, and the values are the number of times each length appears in the list.
For each bar length in lengths, if it's already in the dictionary, we increment its value; otherwise, we initialize it to 1.
Calculating Towers and Heights:

The number of unique lengths (and therefore the number of towers) is simply the size of the dictionary: num_towers = len(frequency).
The height of the tallest tower is the highest value in the dictionary: max_height = max(frequency.values()).
Output the Result:

Print the maximum height and the number of towers.
Example Walkthrough:
Input 1:

5
1 2 2 3 3
Step 1: Count frequencies:
Bar lengths: [1, 2, 2, 3, 3]
Frequencies: {1: 1, 2: 2, 3: 2}
Step 2: Calculate results:
Number of towers = 3 (unique lengths: 1, 2, 3).
Maximum height = 2 (the maximum frequency of any length).
Output 1:

2 3
Input 2:

4
5 5 5 5
Step 1: Count frequencies:
Bar lengths: [5, 5, 5, 5]
Frequencies: {5: 4}
Step 2: Calculate results:
Number of towers = 1 (only one unique length).
Maximum height = 4 (all bars are the same length).
Output 2:

4 1'''