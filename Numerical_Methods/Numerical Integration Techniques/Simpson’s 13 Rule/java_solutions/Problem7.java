import java.util.Scanner;

public class Problem7 {
    // Function to calculate f(x) = x^2
    public static double f(double x) {
        return x * x;
    }

    // Function to calculate f'(x) = 2x
    public static double fPrime(double x) {
        return 2 * x;
    }

    // Function to calculate √(1 + (f'(x))^2)
    public static double integrand(double x) {
        double fPrimeSquared = fPrime(x) * fPrime(x);
        return Math.sqrt(1 + fPrimeSquared);
    }

    // Simpson's 1/3 Rule implementation
    public static double simpsonsRule(double a, double b, int n) {
        if (n % 2 != 0) {
            throw new IllegalArgumentException("Number of intervals must be even");
        }

        double h = (b - a) / n;
        double sum = integrand(a) + integrand(b);

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += (i % 2 == 0) ? 2 * integrand(x) : 4 * integrand(x);
        }

        return (h / 3) * sum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Fixed values for this problem
            double a = 0.0;
            double b = 1.0;
            int n = 8;

            // Calculate using Simpson's 1/3 rule
            double result = simpsonsRule(a, b, n);
            
            // Exact value of arc length
            // For y = x^2, the exact arc length is approximately 1.4789428575445974
            double exactValue = 1.4789428575445974;
            
            // Calculate error
            double error = Math.abs(result - exactValue);

            // Print results
            System.out.println("Arc Length Calculation using Simpson's 1/3 Rule:");
            System.out.println("--------------------------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Approximate arc length: %.10f%n", result);
            System.out.printf("Exact arc length: %.10f%n", exactValue);
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