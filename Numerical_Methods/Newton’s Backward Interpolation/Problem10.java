public class Problem10 {
    public static void main(String[] args) {
        double[] x = {1, 2, 3, 4};
        double[] y = {1, 8, 27, 64};
        double futureX = 5.5;

        NewtonBackwardInterpolation interpolation = new NewtonBackwardInterpolation(x, y);
        double predictedValue = interpolation.interpolate(futureX);

        System.out.printf("Predicted value at x = %.1f is approximately %.2f%n", futureX, predictedValue);
    }
} 