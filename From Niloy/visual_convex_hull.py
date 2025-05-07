import matplotlib.pyplot as plt

# Graham scan code (same as before)
from typing import List, Tuple
import math

def lowest_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    return min(points, key=lambda p: (p[1], p[0]))

def polar_angle(p0: Tuple[int, int], p1: Tuple[int, int]) -> float:
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def cross(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(points) <= 1:
        return points

    pivot = lowest_point(points)
    sorted_points = sorted(points, key=lambda p: (polar_angle(pivot, p), (p[0] - pivot[0])**2 + (p[1] - pivot[1])**2))

    hull = []
    for pt in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], pt) <= 0:
            hull.pop()
        hull.append(pt)

    return hull

# Example set of points
points = [(0, 0), (1, 1), (2, 2), (2,1),(3, 1), (2, 0), (1, -1)]

# Get convex hull
hull = graham_scan(points)
hull.append(hull[0])  # Close the polygon

# Plot
x, y = zip(*points)
hx, hy = zip(*hull)

plt.figure(figsize=(6, 6))
plt.plot(hx, hy, 'r-', lw=2, label='Convex Hull')
plt.plot(x, y, 'bo', label='Points')
plt.plot(*lowest_point(points), 'go', label='Pivot (Lowest Point)')
plt.grid(True)
plt.legend()
plt.title("Graham Scan Convex Hull")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.show()
