public class Problem6 {
    public static void main(String[] args) {
        double h = 0.1;  // Step size
        double x0 = 0.0; // Initial x
        double y0 = 0.0; // Initial y
        double targetX = 0.3; // Target x value
        
        System.out.println("Euler's Method Solution for Problem 6");
        System.out.println("y' = x^2 + y^2, y(0) = 0");
        System.out.println("Step size (h) = " + h);
        System.out.println("\nx\t\ty");
        System.out.println("----------------------------------------");
        
        double x = x0;
        double y = y0;
        
        while (x <= targetX) {
            // Note: This problem doesn't have a simple exact solution
            // We'll just show the numerical solution
            System.out.printf("%.4f\t\t%.4f%n", x, y);
            
            if (x == targetX) break;
            
            // Calculate next y using Euler's method
            double slope = x * x + y * y;  // f(x,y) = x^2 + y^2
            y = y + h * slope;
            x = x + h;
        }
    }
} 