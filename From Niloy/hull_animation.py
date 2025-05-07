import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def cross_product(o, a, b):
    """Returns the cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan_animation(points):
    """Generates steps for the Graham scan convex hull animation."""
    points = sorted(points)  # Sort points by x, then by y
    hull_steps = []  # Stores hull progression at each step

    def process_half(points, hull):
        """Processes one half (lower or upper) of the hull."""
        for p in points:
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
                hull.pop()
                hull_steps.append(hull[:])  # Capture state after removal
            hull.append(p)
            hull_steps.append(hull[:])  # Capture state after addition

    lower, upper = [], []
    process_half(points, lower)  # Construct lower hull
    process_half(reversed(points), upper)  # Construct upper hull

    return hull_steps

# Generate random points for animation
num_points = 10
points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_points)]
hull_steps = graham_scan_animation(points)

# Matplotlib animation setup
fig, ax = plt.subplots()
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.set_title("Graham Scan Convex Hull Animation")
scat = ax.scatter(*zip(*points), color='blue', s=40, label="Points")
line, = ax.plot([], [], 'r-', linewidth=2, label="Convex Hull")

def update(frame):
    """Update function for animation."""
    hull = hull_steps[frame]
    if len(hull) > 1:
        hx, hy = zip(*hull)
        line.set_data(hx + (hx[0],), hy + (hy[0],))  # Close the hull loop
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(hull_steps), interval=500, repeat=False)

plt.legend()
plt.show()
