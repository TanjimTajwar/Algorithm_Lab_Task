import java.util.Scanner;

public class Problem19 {
    // Lagrange Interpolation
    public static double lagrangeInterpolation(double[] x, double[] y, double xValue) {
        double result = 0.0;
        int n = x.length;
        
        for (int i = 0; i < n; i++) {
            double term = y[i];
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    term *= (xValue - x[j]) / (x[i] - x[j]);
                }
            }
            result += term;
        }
        return result;
    }

    // Newton Interpolation
    public static double newtonInterpolation(double[] x, double[] y, double xValue) {
        int n = x.length;
        double[][] dividedDiff = new double[n][n];
        
        // Initialize first column
        for (int i = 0; i < n; i++) {
            dividedDiff[i][0] = y[i];
        }
        
        // Calculate divided differences
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                dividedDiff[i][j] = (dividedDiff[i+1][j-1] - dividedDiff[i][j-1]) / (x[i+j] - x[i]);
            }
        }
        
        // Calculate result
        double result = dividedDiff[0][0];
        double product = 1.0;
        
        for (int i = 1; i < n; i++) {
            product *= (xValue - x[i-1]);
            result += dividedDiff[0][i] * product;
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter number of points: ");
        int n = scanner.nextInt();
        
        double[] x = new double[n];
        double[] y = new double[n];
        
        System.out.println("Enter x values:");
        for (int i = 0; i < n; i++) {
            x[i] = scanner.nextDouble();
        }
        
        System.out.println("Enter y values:");
        for (int i = 0; i < n; i++) {
            y[i] = scanner.nextDouble();
        }
        
        System.out.print("Enter x value to interpolate: ");
        double xValue = scanner.nextDouble();
        
        // Measure execution time for Lagrange
        long startTime = System.nanoTime();
        double lagrangeResult = lagrangeInterpolation(x, y, xValue);
        long lagrangeTime = System.nanoTime() - startTime;
        
        // Measure execution time for Newton
        startTime = System.nanoTime();
        double newtonResult = newtonInterpolation(x, y, xValue);
        long newtonTime = System.nanoTime() - startTime;
        
        System.out.println("\nResults:");
        System.out.println("Lagrange Interpolation: " + lagrangeResult);
        System.out.println("Newton Interpolation: " + newtonResult);
        System.out.println("\nExecution Times:");
        System.out.println("Lagrange: " + lagrangeTime + " nanoseconds");
        System.out.println("Newton: " + newtonTime + " nanoseconds");
        
        scanner.close();
    }
} 