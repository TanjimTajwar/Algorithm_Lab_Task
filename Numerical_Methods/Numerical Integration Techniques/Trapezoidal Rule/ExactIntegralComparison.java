public class Problem4 {
    public static double trapezoidalRule(double a, double b, int n) {
        double h = (b - a) / n;
        double sum = 0.5 * (f(a) + f(b));
        
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += f(x);
        }
        
        return sum * h;
    }
    
    private static double f(double x) {
        return x * x; // f(x) = x^2
    }
    
    private static double exactIntegral(double a, double b) {
        // ∫x^2 dx = (x^3)/3
        return (Math.pow(b, 3) - Math.pow(a, 3)) / 3.0;
    }
    
    public static void main(String[] args) {
        double a = 0;
        double b = 2;
        int n = 4;
        
        double approx = trapezoidalRule(a, b, n);
        double exact = exactIntegral(a, b);
        double error = Math.abs(exact - approx);
        double relativeError = (error / exact) * 100;
        
        System.out.printf("Approximated integral = %.4f%n", approx);
        System.out.printf("Exact integral = %.4f%n", exact);
        System.out.printf("Absolute error = %.4f%n", error);
        System.out.printf("Relative error = %.2f%%%n", relativeError);
    }
} 