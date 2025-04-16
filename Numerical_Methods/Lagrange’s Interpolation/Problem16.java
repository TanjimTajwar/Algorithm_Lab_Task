import java.util.Scanner;

public class Problem16 {
    public static String getPolynomialExpression(double[] x, double[] y) {
        int n = x.length;
        StringBuilder expression = new StringBuilder("f(x) = ");
        
        for (int i = 0; i < n; i++) {
            double coefficient = y[i];
            StringBuilder term = new StringBuilder();
            
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    coefficient /= (x[i] - x[j]);
                    term.append("(x - ").append(x[j]).append(")");
                }
            }
            
            if (i > 0) {
                expression.append(" + ");
            }
            expression.append(coefficient).append(term);
        }
        
        return expression.toString();
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
        
        String polynomial = getPolynomialExpression(x, y);
        System.out.println("Polynomial Expression:");
        System.out.println(polynomial);
        
        scanner.close();
    }
} 