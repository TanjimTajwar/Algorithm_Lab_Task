public class Problem5 {
    public static void main(String[] args) {
        double x0 = 1.0;  // Initial guess
        double tolerance = 0.0001;
        int maxIterations = 10;
        
        System.out.println("Newton-Raphson Method for f(x) = e^x - 3x = 0");
        System.out.println("Initial guess: x₀ = " + x0);
        System.out.println("\nIterations:");
        
        double x = x0;
        for (int i = 0; i < maxIterations; i++) {
            double fx = Math.exp(x) - 3 * x;    // f(x) = e^x - 3x
            double fpx = Math.exp(x) - 3;       // f'(x) = e^x - 3
            
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