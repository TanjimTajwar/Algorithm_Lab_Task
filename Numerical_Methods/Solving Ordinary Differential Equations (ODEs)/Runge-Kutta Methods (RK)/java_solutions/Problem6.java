public class Problem6 {
    public static double f(double x, double y) {
        return x*x + y*y;  // y' = x^2 + y^2
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
        double targetX = 0.8;
        
        double result = rk2(x0, y0, h, targetX);
        System.out.printf("Solution at x = %.1f: y = %.6f%n", targetX, result);
        
        // Note: This problem doesn't have a simple exact solution
        System.out.println("Note: This problem doesn't have a simple exact solution");
    }
} 