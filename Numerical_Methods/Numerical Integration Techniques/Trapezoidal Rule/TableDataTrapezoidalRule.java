public class Problem2 {
    public static double trapezoidalRuleTable(double[] x, double[] y) {
        if (x.length != y.length) {
            throw new IllegalArgumentException("x and y arrays must have same length");
        }
        
        double sum = 0;
        for (int i = 0; i < x.length - 1; i++) {
            double h = x[i + 1] - x[i];
            sum += (y[i] + y[i + 1]) * h / 2;
        }
        
        return sum;
    }
    
    public static void main(String[] args) {
        double[] x = {0, 1, 2};
        double[] y = {1, 3, 7};
        
        double result = trapezoidalRuleTable(x, y);
        System.out.printf("Approximated integral = %.1f%n", result);
    }
} 