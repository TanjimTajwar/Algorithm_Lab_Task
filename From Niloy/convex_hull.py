import matplotlib.pyplot as plt

def cross_product(o, a, b):
    """Returns the cross product of vectors OA and OB.
       > 0 if counter-clockwise, < 0 if clockwise, 0 if collinear."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    """Computes the convex hull of a set of 2D points using Graham's scan."""
    # Sort points by y-coordinate, then by x if equal
    points = sorted(points)

    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Remove last point of each half (duplicate)
    return lower[:-1] + upper[:-1]

# Example usage
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = graham_scan(points)

# Plotting
x, y = zip(*points)
hx, hy = zip(*hull + [hull[0]])  # Closing the hull

plt.scatter(x, y, color='blue')
plt.plot(hx, hy, 'r-', linewidth=2)
plt.show()
