import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else 2  # clockwise or counterclockwise

def distance_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def graham_scan(points):
    if len(points) < 3:
        return points

    min_y = min(points, key=lambda p: (p[1], p[0]))
    points.remove(min_y)

    points.sort(key=lambda p: (
        (p[1] - min_y[1]) / ((p[0] - min_y[0]) + 1e-9),
        distance_sq(min_y, p)
    ))

    hull = [min_y, points[0], points[1]]

    for i in range(2, len(points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    
    return hull

def plot_hull(points, hull):
    # Separate X and Y coordinates
    px, py = zip(*points)
    hx, hy = zip(*(hull + [hull[0]]))  # Close the hull loop

    plt.figure(figsize=(8, 6))
    plt.plot(px, py, 'o', label='Points')
    plt.plot(hx, hy, 'r-', linewidth=2, label='Convex Hull')
    plt.fill(hx, hy, 'r', alpha=0.2)
    plt.legend()
    plt.title('Convex Hull using Graham Scan')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    print("Enter number of points:")
    n = int(input())
    points = []
    print("Enter points as x y (space separated):")
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    hull = graham_scan(points.copy())
    print("\nConvex Hull (in counterclockwise order):")
    for point in hull:
        print(point)

    plot_hull(points, hull)

if __name__ == "__main__":
    main()
