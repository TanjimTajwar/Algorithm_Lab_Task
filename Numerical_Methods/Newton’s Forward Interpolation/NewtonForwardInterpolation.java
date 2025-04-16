import java.util.Arrays;

public class NewtonForwardInterpolation {
    
    // Problem 1: Basic Forward Interpolation
    public static double interpolate(double[] x, double[] y, double targetX) {
        int n = x.length;
        double h = x[1] - x[0]; // step size
        
        // Check if x-values are equidistant
        for (int i = 1; i < n - 1; i++) {
            if (Math.abs((x[i + 1] - x[i]) - h) > 1e-10) {
                throw new IllegalArgumentException("Error: x-values are not equidistant.");
            }
        }
        
        // Calculate forward differences
        double[][] forwardDiff = new double[n][n];
        for (int i = 0; i < n; i++) {
            forwardDiff[i][0] = y[i];
        }
        
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                forwardDiff[i][j] = forwardDiff[i + 1][j - 1] - forwardDiff[i][j - 1];
            }
        }
        
        // Calculate u
        double u = (targetX - x[0]) / h;
        
        // Apply Newton's forward interpolation formula
        double result = forwardDiff[0][0];
        double term = 1;
        for (int i = 1; i < n; i++) {
            term = term * (u - (i - 1)) / i;
            result += term * forwardDiff[0][i];
        }
        
        return result;
    }
    
    // Problem 2: Print Interpolation Table
    public static void printForwardDifferenceTable(double[] x, double[] y) {
        int n = x.length;
        double[][] forwardDiff = new double[n][n];
        
        // Initialize first column
        for (int i = 0; i < n; i++) {
            forwardDiff[i][0] = y[i];
        }
        
        // Calculate forward differences
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                forwardDiff[i][j] = forwardDiff[i + 1][j - 1] - forwardDiff[i][j - 1];
            }
        }
        
        // Print the table
        System.out.println("Forward Difference Table:");
        for (int j = 1; j < n; j++) {
            System.out.print("Δ^" + j + "y: ");
            for (int i = 0; i < n - j; i++) {
                System.out.print(forwardDiff[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    // Problem 3: Find Multiple Interpolated Points
    public static void interpolateMultiplePoints(double[] x, double[] y, double[] targetX) {
        System.out.println("Interpolated values:");
        for (double tx : targetX) {
            try {
                double result = interpolate(x, y, tx);
                System.out.printf("At x = %.1f, y = %.4f%n", tx, result);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    
    // Problem 4: Detect Equidistant Failure
    public static boolean isEquidistant(double[] x) {
        if (x.length < 2) return true;
        double h = x[1] - x[0];
        for (int i = 1; i < x.length - 1; i++) {
            if (Math.abs((x[i + 1] - x[i]) - h) > 1e-10) {
                return false;
            }
        }
        return true;
    }
    
    // Problem 5: Compare Interpolated vs Actual Function
    public static void compareWithActualFunction(double[] x, double[] y, double[] targetX) {
        System.out.println("Comparison of interpolated vs actual values:");
        System.out.println("x\tInterpolated\tActual\tDifference");
        for (double tx : targetX) {
            try {
                double interpolated = interpolate(x, y, tx);
                double actual = Math.sin(tx);
                System.out.printf("%.1f\t%.6f\t%.6f\t%.6f%n", 
                    tx, interpolated, actual, Math.abs(interpolated - actual));
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    
    public static void main(String[] args) {
        // Problem 1
        System.out.println("Problem 1:");
        double[] x1 = {0, 1, 2, 3};
        double[] y1 = {1, 2, 3, 4};
        try {
            double result1 = interpolate(x1, y1, 2.5);
            System.out.printf("Interpolated value at x = 2.5 is %.1f%n", result1);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        
        // Problem 2
        System.out.println("\nProblem 2:");
        double[] x2 = {1, 2, 3, 4};
        double[] y2 = {1, 8, 27, 64};
        printForwardDifferenceTable(x2, y2);
        
        // Problem 3
        System.out.println("\nProblem 3:");
        double[] targetX3 = {1.5, 2.5, 3.5};
        interpolateMultiplePoints(x2, y2, targetX3);
        
        // Problem 4
        System.out.println("\nProblem 4:");
        double[] x4 = {1, 2, 4};
        double[] y4 = {1, 4, 16};
        if (!isEquidistant(x4)) {
            System.out.println("Error: x-values are not equidistant.");
        }
        
        // Problem 5
        System.out.println("\nProblem 5:");
        double[] x5 = {0, Math.PI/6, Math.PI/3, Math.PI/2};
        double[] y5 = new double[x5.length];
        for (int i = 0; i < x5.length; i++) {
            y5[i] = Math.sin(x5[i]);
        }
        double[] targetX5 = {0.3, 0.5, 0.7};
        compareWithActualFunction(x5, y5, targetX5);
    }
} 