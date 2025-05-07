def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    
    # Create list of items: (value per weight, weight, value)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by value per unit weight (descending)
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break  # Knapsack is full

    return total_value


# 👇 USER INPUT SECTION 👇
n = int(input("Enter number of items: "))
values = []
weights = []

print("Enter value and weight for each item:")
for i in range(n):
    v = float(input(f"  Value of item {i+1}: "))
    w = float(input(f"  Weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter capacity of knapsack: "))

# ✅ Solve and output result
max_value = fractional_knapsack(capacity, weights, values)
print(f"\nMaximum value in knapsack = {max_value:.2f}")
