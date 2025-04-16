import java.util.Random;

public class Problem6_OptimizeLargeDataset {
    
    public static double interpolate(double[] x, double[] y, double targetX) {
        int n = x.length;
        double h = x[1] - x[0]; // step size
        
        // Check if x-values are equidistant
        for (int i = 1; i < n - 1; i++) {
            if (Math.abs((x[i + 1] - x[i]) - h) > 1e-10) {
                throw new IllegalArgumentException("Error: x-values are not equidistant.");
            }
        }
        
        // Optimized forward differences calculation
        double[] forwardDiff = new double[n];
        System.arraycopy(y, 0, forwardDiff, 0, n);
        
        // Calculate u
        double u = (targetX - x[0]) / h;
        
        // Apply Newton's forward interpolation formula with optimization
        double result = forwardDiff[0];
        double term = 1;
        
        for (int i = 1; i < n; i++) {
            // Calculate next order differences
            for (int j = 0; j < n - i; j++) {
                forwardDiff[j] = forwardDiff[j + 1] - forwardDiff[j];
            }
            
            // Update result
            term = term * (u - (i - 1)) / i;
            result += term * forwardDiff[0];
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        // Generate large dataset
        int n = 100;
        double[] x = new double[n];
        double[] y = new double[n];
        Random random = new Random();
        
        // Generate equidistant x values
        for (int i = 0; i < n; i++) {
            x[i] = i;
        }
        
        // Generate y values using a function (e.g., sin(x))
        for (int i = 0; i < n; i++) {
            y[i] = Math.sin(x[i]);
        }
        
        // Test interpolation at multiple points
        System.out.println("Testing interpolation with " + n + " data points:");
        double[] testPoints = {25.5, 50.5, 75.5};
        
        for (double point : testPoints) {
            try {
                long startTime = System.nanoTime();
                double result = interpolate(x, y, point);
                long endTime = System.nanoTime();
                
                System.out.printf("At x = %.1f, y = %.6f (Time: %.3f ms)%n", 
                    point, result, (endTime - startTime) / 1_000_000.0);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }
} 