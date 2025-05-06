def newton_raphson(x0, tolerance=0.0001, max_iterations=10):
    x = x0
    print(f"Newton-Raphson Method for f(x) = x² - 4 = 0")
    print(f"Initial guess: x₀ = {x0}")
    print("\nIterations:")
    
    for i in range(max_iterations):
        fx = x * x - 4  # f(x) = x² - 4
        fpx = 2 * x     # f'(x) = 2x
        
        x_next = x - fx / fpx
        
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {fx:.6f}")
        
        if abs(x_next - x) < tolerance:
            print(f"\nRoot found: {x_next:.6f}")
            break
            
        x = x_next

if __name__ == "__main__":
    newton_raphson(2.5)  # Initial guess 