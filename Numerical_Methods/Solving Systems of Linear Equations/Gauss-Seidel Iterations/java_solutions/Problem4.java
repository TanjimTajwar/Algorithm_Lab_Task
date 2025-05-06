public class Problem4 {
    public static void main(String[] args) {
        // System of equations:
        // 4x + y - z = 5
        // x + 3y + z = 6
        // -x + y + 4z = 7
        
        double x = 1.0, y = 1.0, z = 1.0; // Initial values
        double xNew, yNew, zNew;
        double tolerance = 0.001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 4");
        System.out.println("Initial values: x = " + x + ", y = " + y + ", z = " + z);
        System.out.println("Tolerance: " + tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            
            // Calculate new values using Gauss-Seidel formula
            xNew = (5 - y + z) / 4;
            yNew = (6 - xNew - z) / 3;
            zNew = (7 + xNew - yNew) / 4;

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