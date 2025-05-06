import java.util.Scanner;

public class Problem9 {
    // Function to calculate ρ(x) = x^2
    public static double density(double x) {
        return x * x;
    }

    // Function to calculate x^2 * ρ(x) for moment of inertia
    public static double xSquaredDensity(double x) {
        return x * x * density(x);
    }

    // Simpson's 1/3 Rule implementation
    public static double simpsonsRule(double a, double b, int n, boolean isXSquaredDensity) {
        if (n % 2 != 0) {
            throw new IllegalArgumentException("Number of intervals must be even");
        }

        double h = (b - a) / n;
        double sum = isXSquaredDensity ? xSquaredDensity(a) + xSquaredDensity(b) : density(a) + density(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += (i % 2 == 0) ? 
                2 * (isXSquaredDensity ? xSquaredDensity(x) : density(x)) : 
                4 * (isXSquaredDensity ? xSquaredDensity(x) : density(x));
        }

        return (h / 3) * sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Fixed values for this problem
            double a = 0.0;
            double b = 1.0;
            int n = 6;

            // Calculate total mass
            double totalMass = simpsonsRule(a, b, n, false);
            
            // Calculate moment of inertia
            double momentOfInertia = simpsonsRule(a, b, n, true);
            
            // Exact value of moment of inertia
            // For ρ(x) = x^2, the exact moment of inertia is 1/6
            double exactValue = 1.0 / 6.0;
            
            // Calculate error
            double error = Math.abs(momentOfInertia - exactValue);

            // Print results
            System.out.println("Moment of Inertia Calculation using Simpson's 1/3 Rule:");
            System.out.println("----------------------------------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Total mass: %.10f%n", totalMass);
            System.out.printf("Approximate moment of inertia: %.10f%n", momentOfInertia);
            System.out.printf("Exact moment of inertia: %.10f%n", exactValue);
            System.out.printf("Absolute error: %.10f%n", error);
            System.out.printf("Relative error: %.10f%%%n", (error / exactValue) * 100);

            // Show how accuracy changes with different values of n
            System.out.println("\nAccuracy Analysis with Different n Values:");
            System.out.println("----------------------------------------");
            for (int i = 2; i <= 20; i += 2) {
                double approx = simpsonsRule(a, b, i, true);
                double err = Math.abs(approx - exactValue);
                System.out.printf("n = %2d: Error = %.10f%n", i, err);
            }

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
} 