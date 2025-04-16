import java.util.Scanner;

public class Problem17 {
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

    public static void main(String[] args) {
        // Example with 6 points
        double[] x = {1, 2, 3, 4, 5, 6};
        double[] y = {1, 4, 9, 16, 25, 36}; // y = x^2
        
        System.out.println("Testing high-degree polynomial interpolation with 6 points");
        System.out.println("Points:");
        for (int i = 0; i < x.length; i++) {
            System.out.println("(" + x[i] + ", " + y[i] + ")");
        }
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter x value to interpolate: ");
        double xValue = scanner.nextDouble();
        
        long startTime = System.nanoTime();
        double result = lagrangeInterpolation(x, y, xValue);
        long endTime = System.nanoTime();
        
        System.out.println("Interpolated value at x = " + xValue + " is " + result);
        System.out.println("Time taken: " + (endTime - startTime) + " nanoseconds");
        
        scanner.close();
    }
} 