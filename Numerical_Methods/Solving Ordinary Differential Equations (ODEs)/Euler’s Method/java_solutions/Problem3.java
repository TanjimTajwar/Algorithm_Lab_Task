public class Problem3 {
    public static void main(String[] args) {
        double h = 0.1;  // Step size
        double x0 = 0.0; // Initial x
        double y0 = 0.5; // Initial y
        double targetX = 0.3; // Target x value
        
        System.out.println("Euler's Method Solution for Problem 3");
        System.out.println("y' = y^2 - x, y(0) = 0.5");
        System.out.println("Step size (h) = " + h);
        System.out.println("\nx\t\ty\t\tExact\t\tError");
        System.out.println("----------------------------------------");
        
        double x = x0;
        double y = y0;
        
        while (x <= targetX) {
            // Note: This problem doesn't have a simple exact solution
            // We'll just show the numerical solution
            System.out.printf("%.4f\t\t%.4f%n", x, y);
            
            if (x == targetX) break;
            
            // Calculate next y using Euler's method
            double slope = y * y - x;  // f(x,y) = y^2 - x
            y = y + h * slope;
            x = x + h;
        }
    }
} 