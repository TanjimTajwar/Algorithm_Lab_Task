def newton_raphson(x0, tolerance=0.0001, max_iterations=10):
    x = x0
    print(f"Newton-Raphson Method for f(x) = x³ - 2x - 5 = 0")
    print(f"Initial guess: x₀ = {x0}")
    print("\nIterations:")
    
    for i in range(max_iterations):
        fx = x**3 - 2*x - 5  # f(x) = x³ - 2x - 5
        fpx = 3*x**2 - 2     # f'(x) = 3x² - 2
        
        x_next = x - fx / fpx
        
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {fx:.6f}")
        
        if abs(x_next - x) < tolerance:
            print(f"\nRoot found: {x_next:.6f}")
            break
            
        x = x_next

if __name__ == "__main__":
    newton_raphson(2.0)  # Initial guess 