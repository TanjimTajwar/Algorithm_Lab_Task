import java.util.Scanner;

public class Problem18 {
    public static double lagrangeInterpolation(double[] hours, double[] temperatures, double targetHour) {
        double result = 0.0;
        int n = hours.length;
        
        for (int i = 0; i < n; i++) {
            double term = temperatures[i];
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    term *= (targetHour - hours[j]) / (hours[i] - hours[j]);
                }
            }
            result += term;
        }
        return result;
    }

    public static void main(String[] args) {
        // Example temperature data (hours and corresponding temperatures)
        double[] hours = {8, 10, 12, 14, 16, 18};
        double[] temperatures = {20, 22, 25, 24, 23, 21};
        
        System.out.println("Temperature Data:");
        for (int i = 0; i < hours.length; i++) {
            System.out.println("Hour: " + hours[i] + ", Temperature: " + temperatures[i] + "°C");
        }
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter hour to estimate temperature (between 8 and 18): ");
        double targetHour = scanner.nextDouble();
        
        if (targetHour < hours[0] || targetHour > hours[hours.length - 1]) {
            System.out.println("Warning: Extrapolation may not be accurate!");
        }
        
        double estimatedTemp = lagrangeInterpolation(hours, temperatures, targetHour);
        System.out.println("Estimated temperature at " + targetHour + ":00 is " + 
                          String.format("%.2f", estimatedTemp) + "°C");
        
        scanner.close();
    }
} 