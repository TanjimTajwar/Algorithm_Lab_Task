import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class Problem5 {
    private static double f(double x) {
        return x * x; // f(x) = x^2
    }
    
    public static void main(String[] args) {
        double a = 0;
        double b = 2;
        int n = 4;
        double h = (b - a) / n;
        
        // Create dataset for function
        XYSeries functionSeries = new XYSeries("Function");
        XYSeries trapezoidSeries = new XYSeries("Trapezoids");
        
        // Add points for function
        for (double x = a; x <= b; x += 0.01) {
            functionSeries.add(x, f(x));
        }
        
        // Add points for trapezoids
        for (int i = 0; i <= n; i++) {
            double x = a + i * h;
            trapezoidSeries.add(x, f(x));
            if (i < n) {
                trapezoidSeries.add(x + h, f(x + h));
                trapezoidSeries.add(x, 0);
                trapezoidSeries.add(x + h, 0);
                trapezoidSeries.add(x, f(x));
            }
        }
        
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(functionSeries);
        dataset.addSeries(trapezoidSeries);
        
        JFreeChart chart = ChartFactory.createXYLineChart(
            "Trapezoidal Rule Visualization",
            "x",
            "f(x)",
            dataset,
            PlotOrientation.VERTICAL,
            true,
            true,
            false
        );
        
        ChartFrame frame = new ChartFrame("Trapezoidal Rule", chart);
        frame.pack();
        frame.setVisible(true);
    }
} 