def cross_product(o, a, b):
    """Returns the cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    """Computes the convex hull of a set of 2D points."""
    points = sorted(points)  # Sort points by x, then by y

    lower, upper = [], []
    
    for p in points:  # Construct lower hull
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    for p in reversed(points):  # Construct upper hull
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return set(lower[:-1] + upper[:-1])  # Remove duplicates and return as set

# Example usage
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull_points = graham_scan(points)
print(hull_points)  # Outputs a set of points forming the convex hull
