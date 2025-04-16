# Trapezoidal Rule Implementation

This project implements various aspects of the Trapezoidal Rule for numerical integration in Java.

## Problems

1. **Basic Trapezoidal Rule**
   - Implements the basic trapezoidal rule for approximating integrals
   - Sample function: f(x) = x^2
   - File: `BasicTrapezoidalRule.java`

2. **Trapezoidal Rule with Table Data**
   - Implements integration using (x, y) values from a table
   - File: `TableDataTrapezoidalRule.java`

3. **Multiple Intervals**
   - Implements trapezoidal rule for large number of intervals (n = 10,000)
   - Includes performance analysis
   - File: `MultipleIntervalsTrapezoidalRule.java`

4. **Compare with Exact Integral**
   - Computes and compares with exact integral value
   - Calculates absolute and relative errors
   - File: `ExactIntegralComparison.java`

5. **Plot Function and Trapezoids**
   - Visualizes the function and trapezoids under the curve
   - Uses JFreeChart library
   - File: `TrapezoidalVisualization.java`

6. **User-defined Function Input**
   - Allows user to input custom functions
   - Supports basic mathematical operations
   - File: `UserDefinedFunctionTrapezoidalRule.java`

7. **Trapezoidal Rule with Unequal Intervals**
   - Implements trapezoidal rule for data with unequal x-intervals
   - File: `UnequalIntervalsTrapezoidalRule.java`

## Requirements

- Java 11 or higher
- Maven
- JFreeChart library (included in pom.xml)

## Building and Running

1. Clone the repository
2. Run `mvn clean install`
3. Run individual problem files using:
   ```bash
   java -cp target/classes BasicTrapezoidalRule
   java -cp target/classes TableDataTrapezoidalRule
   # ... and so on
   ```

## Notes

- TrapezoidalVisualization.java requires JFreeChart for visualization
- UserDefinedFunctionTrapezoidalRule.java uses JavaScript engine for function evaluation
- All implementations include error handling and input validation 