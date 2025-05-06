public class Problem8 {
    public static double f(double x) {
        return Math.log(x) + x - 2;
    }

    public static Double regularFalsi(double a, double b, double tolerance) {
        if (f(a) * f(b) >= 0) {
            System.out.println("Initial points must have opposite signs");
            return null;
        }

        int iteration = 0;
        while (true) {
            // Calculate new root using Regular Falsi formula
            double c = a - (f(a) * (b - a)) / (f(b) - f(a));

            // Print current iteration details
            System.out.printf("Iteration %d:%n", iteration);
            System.out.printf("a = %.6f, b = %.6f, c = %.6f%n", a, b, c);
            System.out.printf("f(a) = %.6f, f(b) = %.6f, f(c) = %.6f%n", f(a), f(b), f(c));
            System.out.println("-".repeat(50));

            // Check if we've reached the desired accuracy
            if (Math.abs(f(c)) < tolerance) {
                return c;
            }

            // Update interval
            if (f(c) * f(a) < 0) {
                b = c;
            } else {
                a = c;
            }

            iteration++;
        }
    }

    public static void main(String[] args) {
        // Initial interval and tolerance
        double a = 1;
        double b = 2;
        double tolerance = 0.0001;

        // Solve the equation
        Double root = regularFalsi(a, b, tolerance);

        if (root != null) {
            System.out.printf("%nFinal root: %.6f%n", root);
            System.out.printf("f(root) = %.6f%n", f(root));
        }
    }
} 