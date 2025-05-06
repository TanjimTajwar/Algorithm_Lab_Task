public class Problem6 {
    public static void main(String[] args) {
        // System of equations:
        // 3x + 2y - z = 6
        // 2x + 4y + z = 7
        // -x + y + 5z = 8
        
        double x = 1.0, y = 1.0, z = 1.0; // Initial values
        double xNew, yNew, zNew;
        double tolerance = 0.001;
        int iteration = 0;
        boolean converged = false;

        System.out.println("Gauss-Seidel Iteration Method - Problem 6");
        System.out.println("Initial values: x = " + x + ", y = " + y + ", z = " + z);
        System.out.println("Tolerance: " + tolerance);
        System.out.println("\nIterations:");

        while (!converged) {
            iteration++;
            
            // Calculate new values using Gauss-Seidel formula
            xNew = (6 - 2*y + z) / 3;
            yNew = (7 - 2*xNew - z) / 4;
            zNew = (8 + xNew - yNew) / 5;

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