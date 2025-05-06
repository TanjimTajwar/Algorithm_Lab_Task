public class Problem9 {
    public static void main(String[] args) {
        double x0 = 1.0;  // Initial guess
        double tolerance = 0.0001;
        int maxIterations = 10;
        
        System.out.println("Newton-Raphson Method for f(x) = x⁵ - 3x + 1 = 0");
        System.out.println("Initial guess: x₀ = " + x0);
        System.out.println("\nIterations:");
        
        double x = x0;
        for (int i = 0; i < maxIterations; i++) {
            double fx = Math.pow(x, 5) - 3 * x + 1;  // f(x) = x⁵ - 3x + 1
            double fpx = 5 * Math.pow(x, 4) - 3;     // f'(x) = 5x⁴ - 3
            
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