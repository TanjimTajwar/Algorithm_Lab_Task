import java.util.Scanner;

public class Problem15 {
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
        
        double result = lagrangeInterpolation(x, y, xValue);
        System.out.println("Interpolated value at x = " + xValue + " is " + result);
        
        scanner.close();
    }
} 