public class Problem5 {
    public static void main(String[] args) {
        // System of equations:
        // 6x + y + z = 8
        // x + 5y + z = 9
        // x + y + 4z = 10
        
        double x = 0.0, y = 0.0, z = 0.0; // Initial values
        double xNew, yNew, zNew;
        double tolerance = 0.0001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 5");
        System.out.println("Initial values: x = " + x + ", y = " + y + ", z = " + z);
        System.out.println("Tolerance: " + tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            
            // Calculate new values using Gauss-Seidel formula
            xNew = (8 - y - z) / 6;
            yNew = (9 - xNew - z) / 5;
            zNew = (10 - xNew - yNew) / 4;

            // Check for convergence
            if (Math.abs(xNew - x) < tolerance &&
                Math.abs(yNew - y) < tolerance &&
                Math.abs(zNew - z) < tolerance) {
                converged = true;
            }

            // Update values
            x = xNew;
            y = yNew;
            z = zNew;

            // Print current iteration
            System.out.printf("Iteration %d: x = %.6f, y = %.6f, z = %.6f%n", 
                            iteration, x, y, z);
        }

        System.out.println("\nSolution converged after " + iteration + " iterations:");
        System.out.printf("x = %.6f%n", x);
        System.out.printf("y = %.6f%n", y);
        System.out.printf("z = %.6f%n", z);
    }
} 