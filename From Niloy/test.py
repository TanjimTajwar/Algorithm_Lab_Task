def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_gcd(arr):
    max_gcd_value = 0
    n = len(arr)
    
    # Check the GCD of every pair
    for i in range(n):
        for j in range(i + 1, n):
            max_gcd_value = max(max_gcd_value, gcd(arr[i], arr[j]))
    
    return max_gcd_value

# Example usage
arr = [1, 10, 11]
print("Maximum GCD is:", max_gcd(arr))
