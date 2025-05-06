public class Problem10 {
    public static double f(double x, double y) {
        return Math.exp(-x) + y;  // y' = e^(-x) + y
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
        double y0 = 0;
        double h = 0.2;
        double targetX = 0.8;
        
        double result = rk2(x0, y0, h, targetX);
        System.out.printf("Solution at x = %.1f: y = %.6f%n", targetX, result);
        
        // Exact solution: y = x*e^(-x) + e^x - 1
        double exact = targetX*Math.exp(-targetX) + Math.exp(targetX) - 1;
        System.out.printf("Exact solution: y = %.6f%n", exact);
        System.out.printf("Error: %.6f%n", Math.abs(result - exact));
    }
} 