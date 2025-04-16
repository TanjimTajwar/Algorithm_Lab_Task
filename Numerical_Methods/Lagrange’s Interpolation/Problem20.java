import java.util.Scanner;

public class Problem20 {
    public static String getSymbolicLagrangeFormula(double[] x, double[] y) {
        int n = x.length;
        StringBuilder formula = new StringBuilder("L(x) = ");
        
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                formula.append(" + ");
            }
            
            // Add y[i]
            formula.append(y[i]);
            
            // Add the product terms
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    formula.append(" * (x - ").append(x[j]).append(")/(")
                           .append(x[i]).append(" - ").append(x[j]).append(")");
                }
            }
        }
        
        return formula.toString();
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
        
        String formula = getSymbolicLagrangeFormula(x, y);
        System.out.println("\nExact Lagrange Formula:");
        System.out.println(formula);
        
        scanner.close();
    }
} 