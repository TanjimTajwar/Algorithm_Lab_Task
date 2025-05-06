import java.util.Scanner;

public class Problem5 {
    // Function to calculate F(x) = 2x + 3
    public static double f(double x) {
        return 2 * x + 3;
    }

    // Simpson's 1/3 Rule implementation
    public static double simpsonsRule(double a, double b, int n) {
        if (n % 2 != 0) {
            throw new IllegalArgumentException("Number of intervals must be even");
        }

        double h = (b - a) / n;
        double sum = f(a) + f(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += (i % 2 == 0) ? 2 * f(x) : 4 * f(x);
        }

        return (h / 3) * sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Fixed values for this problem
            double a = 0.0;
            double b = 5.0;
            int n = 10;

            // Calculate using Simpson's 1/3 rule
            double result = simpsonsRule(a, b, n);
            
            // Exact value of ∫(2x + 3)dx from 0 to 5 is [x^2 + 3x]₀⁵ = 40
            double exactValue = 40.0;
            
            // Calculate error
            double error = Math.abs(result - exactValue);

            // Print results
            System.out.println("Work Done Calculation using Simpson's 1/3 Rule:");
            System.out.println("--------------------------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Approximate work done: %.10f%n", result);
            System.out.printf("Exact work done: %.10f%n", exactValue);
            System.out.printf("Absolute error: %.10f%n", error);
            System.out.printf("Relative error: %.10f%%%n", (error / exactValue) * 100);

            // Show how accuracy changes with different values of n
            System.out.println("\nAccuracy Analysis with Different n Values:");
            System.out.println("----------------------------------------");
            for (int i = 2; i <= 20; i += 2) {
                double approx = simpsonsRule(a, b, i);
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