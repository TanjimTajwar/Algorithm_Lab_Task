public class Problem14 {
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
        double[] x = {1, 2, 4};
        double[] y = {1, 4, 16};
        double xValue = 3;
        
        double result = lagrangeInterpolation(x, y, xValue);
        System.out.println("Interpolated value at x = " + xValue + " is " + result);
    }
} 