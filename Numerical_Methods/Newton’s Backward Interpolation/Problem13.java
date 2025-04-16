import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Problem13 {
    public static void main(String[] args) {
        try {
            // Read input from file
            List<Double> xList = new ArrayList<>();
            List<Double> yList = new ArrayList<>();
            
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");
                xList.add(Double.parseDouble(parts[0]));
                yList.add(Double.parseDouble(parts[1]));
            }
            reader.close();

            // Convert lists to arrays
            double[] x = new double[xList.size()];
            double[] y = new double[yList.size()];
            for (int i = 0; i < xList.size(); i++) {
                x[i] = xList.get(i);
                y[i] = yList.get(i);
            }

            // Perform interpolation
            NewtonBackwardInterpolation interpolation = new NewtonBackwardInterpolation(x, y);
            double xValue = 3.8;
            double result = interpolation.interpolate(xValue);

            // Write result to output file
            BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"));
            writer.write(String.format("Interpolated value at x = %.1f is approximately %.2f", xValue, result));
            writer.close();

            System.out.println("Result has been written to output.txt");

        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
} 