public class Problem12 {
    public static void main(String[] args) {
        double[] x = {1, 2, 3, 4};
        double[] y = new double[x.length];
        
        // Calculate y values using f(x) = x³ + 1
        for (int i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], 3) + 1;
        }

        double testX = 2.5;
        double actualValue = Math.pow(testX, 3) + 1;

        NewtonBackwardInterpolation interpolation = new NewtonBackwardInterpolation(x, y);
        double error = interpolation.estimateError(testX, actualValue);

        System.out.printf("Error estimation for f(x) = x³ + 1 at x = %.1f%n", testX);
        System.out.printf("Actual value: %.4f%n", actualValue);
        System.out.printf("Interpolated value: %.4f%n", interpolation.interpolate(testX));
        System.out.printf("Absolute error: %.4f%n", error);
    }
} 