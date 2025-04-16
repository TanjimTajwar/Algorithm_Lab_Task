public class Problem3 {
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
    
    public static void main(String[] args) {
        double a = 0;
        double b = 2;
        int n = 10000;
        
        long startTime = System.nanoTime();
        double result = trapezoidalRule(a, b, n);
        long endTime = System.nanoTime();
        
        double executionTime = (endTime - startTime) / 1_000_000.0; // Convert to milliseconds
        
        System.out.printf("Approximated integral = %.4f%n", result);
        System.out.printf("Execution time: %.2f ms%n", executionTime);
    }
} 