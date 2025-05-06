public class Problem2 {
    public static double f(double x, double y) {
        return 2*x - y;  // y' = 2x - y
    }

    public static double rk2(double x0, double y0, double h, double targetX) {
        double x = x0;
        double y = y0;
        
        while (x < targetX) {
            double k1 = h * f(x, y);
            double k2 = h * f(x + h, y + k1);
            
            y = y + (k1 + k2) / 2;
            x = x + h;
        }
        
        return y;
    }

    public static void main(String[] args) {
        double x0 = 0;
        double y0 = 1;
        double h = 0.2;
        double targetX = 1.0;
        
        double result = rk2(x0, y0, h, targetX);
        System.out.printf("Solution at x = %.1f: y = %.6f%n", targetX, result);
        
        // Exact solution: y = 2x - 2 + 3e^(-x)
        double exact = 2*targetX - 2 + 3*Math.exp(-targetX);
        System.out.printf("Exact solution: y = %.6f%n", exact);
        System.out.printf("Error: %.6f%n", Math.abs(result - exact));
    }
} 