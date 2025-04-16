public class NewtonBackwardInterpolation {
    private double[] x;
    private double[] y;
    private double[][] backwardDiff;

    public NewtonBackwardInterpolation(double[] x, double[] y) {
        this.x = x;
        this.y = y;
        this.backwardDiff = new double[x.length][x.length];
        calculateBackwardDifferences();
    }

    private void calculateBackwardDifferences() {
        int n = x.length;
        for (int i = 0; i < n; i++) {
            backwardDiff[i][0] = y[i];
        }

        for (int j = 1; j < n; j++) {
            for (int i = n - 1; i >= j; i--) {
                backwardDiff[i][j] = backwardDiff[i][j-1] - backwardDiff[i-1][j-1];
            }
        }
    }

    public double interpolate(double xValue) {
        double h = x[1] - x[0];
        double p = (xValue - x[x.length - 1]) / h;
        double result = backwardDiff[x.length - 1][0];
        double term = 1.0;

        for (int i = 1; i < x.length; i++) {
            term *= (p + i - 1) / i;
            result += term * backwardDiff[x.length - 1][i];
        }

        return result;
    }

    public void printBackwardDifferenceTable() {
        System.out.println("Backward Difference Table:");
        System.out.println("x\t\ty\t\tΔy\t\tΔ²y\t\tΔ³y");
        for (int i = 0; i < x.length; i++) {
            System.out.printf("%.2f\t\t%.2f\t\t", x[i], backwardDiff[i][0]);
            for (int j = 1; j <= i; j++) {
                System.out.printf("%.2f\t\t", backwardDiff[i][j]);
            }
            System.out.println();
        }
    }

    public double estimateError(double xValue, double actualValue) {
        double interpolatedValue = interpolate(xValue);
        return Math.abs(actualValue - interpolatedValue);
    }
} 