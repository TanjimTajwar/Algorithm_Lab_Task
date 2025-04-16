import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Problem6 {
    public static double evaluateFunction(String function, double x) {
        // Replace x with the actual value
        String expression = function.replaceAll("x", String.valueOf(x));
        
        // Handle basic operations
        expression = expression.replaceAll("\\^", "**");
        
        // Use JavaScript engine to evaluate the expression
        try {
            javax.script.ScriptEngineManager manager = new javax.script.ScriptEngineManager();
            javax.script.ScriptEngine engine = manager.getEngineByName("js");
            return Double.parseDouble(engine.eval(expression).toString());
        } catch (Exception e) {
            throw new IllegalArgumentException("Invalid function expression");
        }
    }
    
    public static double trapezoidalRule(String function, double a, double b, int n) {
        double h = (b - a) / n;
        double sum = 0.5 * (evaluateFunction(function, a) + evaluateFunction(function, b));
        
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            sum += evaluateFunction(function, x);
        }
        
        return sum * h;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter function (e.g., x^2 + 3*x + 1): ");
        String function = scanner.nextLine();
        
        System.out.print("Enter lower limit (a): ");
        double a = scanner.nextDouble();
        
        System.out.print("Enter upper limit (b): ");
        double b = scanner.nextDouble();
        
        System.out.print("Enter number of intervals (n): ");
        int n = scanner.nextInt();
        
        double result = trapezoidalRule(function, a, b, n);
        System.out.printf("Approximated integral = %.4f%n", result);
        
        scanner.close();
    }
} 