public class Problem10 {
    public static void main(String[] args) {
        double h = 0.1;  // Step size
        double x0 = 0.0; // Initial x
        double y0 = 1.0; // Initial y
        double targetX = 0.4; // Target x value
        
        System.out.println("Euler's Method Solution for Problem 10");
        System.out.println("y' = 2y - x, y(0) = 1");
        System.out.println("Step size (h) = " + h);
        System.out.println("\nx\t\ty\t\tExact\t\tError");
        System.out.println("----------------------------------------");
        
        double x = x0;
        double y = y0;
        
        while (x <= targetX) {
            // Calculate exact solution: y = (x/2 + 1/4) + (3/4)e^(2x)
            double exact = (x/2 + 0.25) + 0.75 * Math.exp(2*x);
            double error = Math.abs(exact - y);
            
            System.out.printf("%.4f\t\t%.4f\t\t%.4f\t\t%.4f%n", x, y, exact, error);
            
            if (x == targetX) break;
            
            // Calculate next y using Euler's method
            double slope = 2 * y - x;  // f(x,y) = 2y - x
            y = y + h * slope;
            x = x + h;
        }
    }
} 