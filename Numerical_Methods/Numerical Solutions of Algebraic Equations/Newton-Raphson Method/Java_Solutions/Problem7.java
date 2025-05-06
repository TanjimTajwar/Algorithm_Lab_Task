public class Problem7 {
    public static void main(String[] args) {
        double x0 = 1.5;  // Initial guess
        double tolerance = 0.0001;
        int maxIterations = 10;
        
        System.out.println("Newton-Raphson Method for f(x) = x³ + 4x² - 10 = 0");
        System.out.println("Initial guess: x₀ = " + x0);
        System.out.println("\nIterations:");
        
        double x = x0;
        for (int i = 0; i < maxIterations; i++) {
            double fx = x * x * x + 4 * x * x - 10;  // f(x) = x³ + 4x² - 10
            double fpx = 3 * x * x + 8 * x;          // f'(x) = 3x² + 8x
            
            double xNext = x - fx / fpx;
            
            System.out.printf("Iteration %d: x = %.6f, f(x) = %.6f\n", 
                            i + 1, x, fx);
            
            if (Math.abs(xNext - x) < tolerance) {
                System.out.printf("\nRoot found: %.6f\n", xNext);
                break;
            }
            
            x = xNext;
        }
    }
} 