public class Problem7 {
    public static double f(double x, double y) {
        return 2*x*y;  // y' = 2xy
    }

    public static double rk4(double x0, double y0, double h, double targetX) {
        double x = x0;
        double y = y0;
        
        while (x < targetX) {
            double k1 = h * f(x, y);
            double k2 = h * f(x + h/2, y + k1/2);
            double k3 = h * f(x + h/2, y + k2/2);
            double k4 = h * f(x + h, y + k3);
            
            y = y + (k1 + 2*k2 + 2*k3 + k4) / 6;
            x = x + h;
        }
        
        return y;
    }

    public static void main(String[] args) {
        double x0 = 0;
        double y0 = 1;
        double h = 0.1;
        double targetX = 0.5;
        
        double result = rk4(x0, y0, h, targetX);
        System.out.printf("Solution at x = %.1f: y = %.6f%n", targetX, result);
        
        // Exact solution: y = e^(x^2)
        double exact = Math.exp(targetX*targetX);
        System.out.printf("Exact solution: y = %.6f%n", exact);
        System.out.printf("Error: %.6f%n", Math.abs(result - exact));
    }
} 