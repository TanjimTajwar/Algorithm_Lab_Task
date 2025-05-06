import java.util.Scanner;

public class Problem6 {
    // Function to calculate ρ(x) = 1 + x^2
    public static double density(double x) {
        return 1 + x * x;
    }

    // Function to calculate x * ρ(x) for center of mass
    public static double xDensity(double x) {
        return x * density(x);
    }

    // Simpson's 1/3 Rule implementation
    public static double simpsonsRule(double a, double b, int n, boolean isXDensity) {
        if (n % 2 != 0) {
            throw new IllegalArgumentException("Number of intervals must be even");
        }

        double h = (b - a) / n;
        double sum = isXDensity ? xDensity(a) + xDensity(b) : density(a) + density(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += (i % 2 == 0) ? 
                2 * (isXDensity ? xDensity(x) : density(x)) : 
                4 * (isXDensity ? xDensity(x) : density(x));
        }

        return (h / 3) * sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Fixed values for this problem
            double a = 0.0;
            double b = 2.0;
            int n = 6;

            // Calculate total mass
            double totalMass = simpsonsRule(a, b, n, false);
            
            // Calculate first moment
            double firstMoment = simpsonsRule(a, b, n, true);
            
            // Calculate center of mass
            double centerOfMass = firstMoment / totalMass;
            
            // Exact value of center of mass
            // For ρ(x) = 1 + x^2, the exact center of mass is at x = 1.5
            double exactValue = 1.5;
            
            // Calculate error
            double error = Math.abs(centerOfMass - exactValue);

            // Print results
            System.out.println("Center of Mass Calculation using Simpson's 1/3 Rule:");
            System.out.println("------------------------------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Total mass: %.10f%n", totalMass);
            System.out.printf("First moment: %.10f%n", firstMoment);
            System.out.printf("Approximate center of mass: %.10f%n", centerOfMass);
            System.out.printf("Exact center of mass: %.10f%n", exactValue);
            System.out.printf("Absolute error: %.10f%n", error);
            System.out.printf("Relative error: %.10f%%%n", (error / exactValue) * 100);

            // Show how accuracy changes with different values of n
            System.out.println("\nAccuracy Analysis with Different n Values:");
            System.out.println("----------------------------------------");
            for (int i = 2; i <= 20; i += 2) {
                double mass = simpsonsRule(a, b, i, false);
                double moment = simpsonsRule(a, b, i, true);
                double approx = moment / mass;
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