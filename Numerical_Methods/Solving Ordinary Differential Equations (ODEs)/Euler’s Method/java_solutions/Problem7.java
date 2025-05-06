public class Problem7 {
    public static void main(String[] args) {
        double h = 0.2;  // Step size
        double x0 = 0.0; // Initial x
        double y0 = 1.0; // Initial y
        double targetX = 0.6; // Target x value
        
        System.out.println("Euler's Method Solution for Problem 7");
        System.out.println("y' = xy + 1, y(0) = 1");
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
            double slope = x * y + 1;  // f(x,y) = xy + 1
            y = y + h * slope;
            x = x + h;
        }
    }
} 