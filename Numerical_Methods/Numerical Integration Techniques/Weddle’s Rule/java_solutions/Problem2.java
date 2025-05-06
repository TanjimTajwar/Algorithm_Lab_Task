public class Problem2 {
    public static double f(double x) {
        return Math.sin(x);
    }

    public static double weddlesRule(double a, double b, int n) {
        if (n % 6 != 0) {
            throw new IllegalArgumentException("Number of intervals must be divisible by 6");
        }

        double h = (b - a) / n;
        double sum1 = f(a) + f(b);  // First and last terms
        double sum2 = 0, sum3 = 0, sum4 = 0, sum5 = 0;

        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 6 == 1) {
                sum2 += f(x);
            } else if (i % 6 == 2 || i % 6 == 4) {
                sum3 += f(x);
            } else if (i % 6 == 3) {
                sum4 += f(x);
            } else if (i % 6 == 5) {
                sum5 += f(x);
            }
        }

        sum2 *= 5;
        sum4 *= 6;
        sum5 *= 5;

        return (3 * h / 10) * (sum1 + sum2 + sum3 + sum4 + sum5);
    }

    public static void main(String[] args) {
        double a = 0;           // Lower limit
        double b = Math.PI/2;   // Upper limit
        int n = 6;             // Number of intervals

        try {
            double result = weddlesRule(a, b, n);
            double exactValue = -Math.cos(b) + Math.cos(a);  // Integral of sin(x) is -cos(x)
            double error = Math.abs(result - exactValue);

            System.out.printf("Approximate value using Weddle's Rule: %.6f%n", result);
            System.out.printf("Exact value: %.6f%n", exactValue);
            System.out.printf("Absolute error: %.6f%n", error);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
} 