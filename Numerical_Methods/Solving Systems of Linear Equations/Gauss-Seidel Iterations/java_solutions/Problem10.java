public class Problem10 {
    public static void main(String[] args) {
        // System of equations:
        // 7x + y + z = 11
        // x + 6y + z = 12
        // x + y + 5z = 13
        
        // Initial values
        double x = 0.0, y = 0.0, z = 0.0;
        double tolerance = 0.0001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 10");
        System.out.printf("Initial values: x = %.6f, y = %.6f, z = %.6f%n", x, y, z);
        System.out.printf("Tolerance: %.6f%n", tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            double xOld = x;
            double yOld = y;
            double zOld = z;

            // Calculate new values using Gauss-Seidel formula
            x = (11 - y - z) / 7;
            y = (12 - x - z) / 6;
            z = (13 - x - y) / 5;

            // Check for convergence
            if (Math.abs(x - xOld) < tolerance &&
                Math.abs(y - yOld) < tolerance &&
                Math.abs(z - zOld) < tolerance) {
                converged = true;
            }

            // Print current iteration
            System.out.printf("Iteration %d: x = %.6f, y = %.6f, z = %.6f%n", 
                            iteration, x, y, z);
        }

        System.out.printf("%nSolution converged after %d iterations:%n", iteration);
        System.out.printf("x = %.6f%n", x);
        System.out.printf("y = %.6f%n", y);
        System.out.printf("z = %.6f%n", z);
    }
} 