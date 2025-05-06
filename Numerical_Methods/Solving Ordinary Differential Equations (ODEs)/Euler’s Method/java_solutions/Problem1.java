public class Problem1 {
    public static void main(String[] args) {
        double h = 0.1;  // Step size
        double x0 = 0.0; // Initial x
        double y0 = 1.0; // Initial y
        double targetX = 0.5; // Target x value
        
        System.out.println("Euler's Method Solution for Problem 1");
        System.out.println("y' = x + y, y(0) = 1");
        System.out.println("Step size (h) = " + h);
        System.out.println("\nx\t\ty\t\tExact\t\tError");
        System.out.println("----------------------------------------");
        
        double x = x0;
        double y = y0;
        
        while (x <= targetX) {
            // Calculate exact solution: y = 2e^x - x - 1
            double exact = 2 * Math.exp(x) - x - 1;
            double error = Math.abs(exact - y);
            
            System.out.printf("%.4f\t\t%.4f\t\t%.4f\t\t%.4f%n", x, y, exact, error);
            
            if (x == targetX) break;
            
            // Calculate next y using Euler's method
            double slope = x + y;  // f(x,y) = x + y
            y = y + h * slope;
            x = x + h;
        }
    }
} 