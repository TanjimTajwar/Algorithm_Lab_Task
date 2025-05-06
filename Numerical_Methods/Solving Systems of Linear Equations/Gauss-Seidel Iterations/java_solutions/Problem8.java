public class Problem8 {
    public static void main(String[] args) {
        // System of equations:
        // 4x + 2y - z = 7
        // 2x + 5y + z = 8
        // -x + y + 4z = 9
        
        double x = 1.0, y = 1.0, z = 1.0; // Initial values
        double xNew, yNew, zNew;
        double tolerance = 0.001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 8");
        System.out.println("Initial values: x = " + x + ", y = " + y + ", z = " + z);
        System.out.println("Tolerance: " + tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            
            // Calculate new values using Gauss-Seidel formula
            xNew = (7 - 2*y + z) / 4;
            yNew = (8 - 2*xNew - z) / 5;
            zNew = (9 + xNew - yNew) / 4;

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