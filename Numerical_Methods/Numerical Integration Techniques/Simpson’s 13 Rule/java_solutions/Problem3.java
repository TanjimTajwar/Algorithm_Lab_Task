import java.util.Scanner;

public class Problem3 {
    // Function to calculate f(x) = e^x
    public static double f(double x) {
        return Math.exp(x);
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
            
            // Get number of intervals from user
            System.out.print("Enter number of intervals (must be even): ");
            int n = scanner.nextInt();
            
            if (n % 2 != 0) {
                throw new IllegalArgumentException("Number of intervals must be even");
            }

            // Calculate using Simpson's 1/3 rule
            double result = simpsonsRule(a, b, n);
            
            // Exact value of ∫e^x dx from 0 to 1 is e - 1
            double exactValue = Math.E - 1;
            
            // Calculate error
            double error = Math.abs(result - exactValue);

            // Print results
            System.out.println("\nSimpson's 1/3 Rule Results:");
            System.out.println("---------------------------");
            System.out.printf("Number of intervals (n): %d%n", n);
            System.out.printf("Approximate value: %.10f%n", result);
            System.out.printf("Exact value: %.10f%n", exactValue);
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