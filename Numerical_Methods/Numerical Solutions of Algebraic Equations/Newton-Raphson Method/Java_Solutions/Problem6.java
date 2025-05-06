public class Problem6 {
    public static void main(String[] args) {
        double x0 = 7.0;  // Initial guess
        double tolerance = 0.0001;
        int maxIterations = 10;
        
        System.out.println("Newton-Raphson Method for f(x) = ln(x) - 2 = 0");
        System.out.println("Initial guess: x₀ = " + x0);
        System.out.println("\nIterations:");
        
        double x = x0;
        for (int i = 0; i < maxIterations; i++) {
            double fx = Math.log(x) - 2;    // f(x) = ln(x) - 2
            double fpx = 1.0 / x;           // f'(x) = 1/x
            
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