public class Problem11 {
    public static void main(String[] args) {
        double[] x = {1, 2, 3, 4};
        double[] y = {1, 8, 27, 64};
        double midpointX = 2.5;

        NewtonBackwardInterpolation backwardInterpolation = new NewtonBackwardInterpolation(x, y);
        double backwardResult = backwardInterpolation.interpolate(midpointX);

        // For forward interpolation, we'll use the same class but with reversed arrays
        double[] reversedX = new double[x.length];
        double[] reversedY = new double[y.length];
        for (int i = 0; i < x.length; i++) {
            reversedX[i] = x[x.length - 1 - i];
            reversedY[i] = y[y.length - 1 - i];
        }
        NewtonBackwardInterpolation forwardInterpolation = new NewtonBackwardInterpolation(reversedX, reversedY);
        double forwardResult = forwardInterpolation.interpolate(midpointX);

        System.out.println("Comparison of Forward and Backward Interpolation at x = " + midpointX);
        System.out.printf("Forward Interpolation result: %.4f%n", forwardResult);
        System.out.printf("Backward Interpolation result: %.4f%n", backwardResult);
        System.out.printf("Difference: %.4f%n", Math.abs(forwardResult - backwardResult));
    }
} 