public class Problem2 {
    public static void main(String[] args) {
        // System of equations:
        // 3x - y + z = 4
        // -x + 4y + 2z = 5
        // x + 2y + 5z = 6
        
        double x = 1.0, y = 1.0, z = 1.0; // Initial values
        double xNew, yNew, zNew;
        double tolerance = 0.001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 2");
        System.out.println("Initial values: x = " + x + ", y = " + y + ", z = " + z);
        System.out.println("Tolerance: " + tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            
            // Calculate new values using Gauss-Seidel formula
            xNew = (4 + y - z) / 3;
            yNew = (5 + xNew - 2*z) / 4;
            zNew = (6 - xNew - 2*yNew) / 5;

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