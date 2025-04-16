public class Problem8 {
    public static void main(String[] args) {
        double[] x = {1, 2, 3, 4};
        double[] y = {1, 8, 27, 64};
        double xValue = 3.8;

        NewtonBackwardInterpolation interpolation = new NewtonBackwardInterpolation(x, y);
        double result = interpolation.interpolate(xValue);

        System.out.printf("Interpolated value at x = %.1f is approximately %.2f%n", xValue, result);
    }
} 