public class Problem9 {
    public static void main(String[] args) {
        double[] x = {1, 2, 3, 4};
        double[] y = {1, 8, 27, 64};

        NewtonBackwardInterpolation interpolation = new NewtonBackwardInterpolation(x, y);
        interpolation.printBackwardDifferenceTable();
    }
} 