public class Problem4 {
    public static double f(double x, double y) {
        return Math.exp(x) - y;  // y' = e^x - y
    }

    public static double rk3(double x0, double y0, double h, double targetX) {
        double x = x0;
        double y = y0;
        
        while (x < targetX) {
            double k1 = h * f(x, y);
            double k2 = h * f(x + h/2, y + k1/2);
            double k3 = h * f(x + h, y - k1 + 2*k2);
            
            y = y + (k1 + 4*k2 + k3) / 6;
            x = x + h;
        }
        
        return y;
    }

    public static void main(String[] args) {
        double x0 = 0;
        double y0 = 1;
        double h = 0.2;
        double targetX = 0.6;
        
        double result = rk3(x0, y0, h, targetX);
        System.out.printf("Solution at x = %.1f: y = %.6f%n", targetX, result);
        
        // Exact solution: y = (x*e^x + y0)
        double exact = targetX*Math.exp(targetX) + y0;
        System.out.printf("Exact solution: y = %.6f%n", exact);
        System.out.printf("Error: %.6f%n", Math.abs(result - exact));
    }
} 