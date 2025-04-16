public class Problem7 {
    public static double trapezoidalRuleUnequal(double[] x, double[] y) {
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
        // Example with unequal intervals
        double[] x = {0, 0.5, 1.2, 1.8, 2.0};
        double[] y = new double[x.length];
        
        // Calculate y values for f(x) = x^2
        for (int i = 0; i < x.length; i++) {
            y[i] = x[i] * x[i];
        }
        
        double result = trapezoidalRuleUnequal(x, y);
        System.out.printf("Approximated integral with unequal intervals = %.4f%n", result);
        
        // Compare with equal intervals
        double a = x[0];
        double b = x[x.length - 1];
        int n = x.length - 1;
        double h = (b - a) / n;
        
        double[] xEqual = new double[n + 1];
        double[] yEqual = new double[n + 1];
        
        for (int i = 0; i <= n; i++) {
            xEqual[i] = a + i * h;
            yEqual[i] = xEqual[i] * xEqual[i];
        }
        
        double resultEqual = trapezoidalRuleUnequal(xEqual, yEqual);
        System.out.printf("Approximated integral with equal intervals = %.4f%n", resultEqual);
    }
} 