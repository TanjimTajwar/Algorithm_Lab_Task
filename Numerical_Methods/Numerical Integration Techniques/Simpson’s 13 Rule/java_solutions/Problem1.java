import java.util.Scanner;

public class Problem1 {
    // Function to calculate f(x) = x^2
    public static double f(double x) {
        return x * x;
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
            double b = 1.0;
            int n = 4;

            // Calculate using Simpson's 1/3 rule
            double result = simpsonsRule(a, b, n);
            
            // Exact value of ∫x^2 dx from 0 to 1 is 1/3
            double exactValue = 1.0 / 3.0;
            
            // Calculate error
            double error = Math.abs(result - exactValue);

            // Print results
            System.out.println("Simpson's 1/3 Rule Results:");
            System.out.println("---------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Approximate value: %.10f%n", result);
            System.out.printf("Exact value: %.10f%n", exactValue);
            System.out.printf("Absolute error: %.10f%n", error);
            System.out.printf("Relative error: %.10f%%%n", (error / exactValue) * 100);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
} 