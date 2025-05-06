import math

def newton_raphson(x0, tolerance=0.0001, max_iterations=10):
    x = x0
    print(f"Newton-Raphson Method for f(x) = sin(x) - x/2 = 0")
    print(f"Initial guess: x₀ = {x0}")
    print("\nIterations:")
    
    for i in range(max_iterations):
        fx = math.sin(x) - x/2        # f(x) = sin(x) - x/2
        fpx = math.cos(x) - 0.5       # f'(x) = cos(x) - 0.5
        
        x_next = x - fx / fpx
        
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {fx:.6f}")
        
        if abs(x_next - x) < tolerance:
            print(f"\nRoot found: {x_next:.6f}")
            break
            
        x = x_next

if __name__ == "__main__":
    newton_raphson(1.0)  # Initial guess 