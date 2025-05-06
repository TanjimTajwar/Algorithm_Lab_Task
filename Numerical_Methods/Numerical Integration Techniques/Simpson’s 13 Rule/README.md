# Simpson's 1/3 Rule Programming Problems

This repository contains solutions to 10 programming problems using Simpson's 1/3 Rule for numerical integration. Each problem is implemented in both Java and Python (using NumPy).

## Problems

1. **Definite Integral of x²**
   - Calculate ∫x² dx from 0 to 1
   - Compare with exact value (1/3)
   - Uses n = 4 intervals

2. **Area Under Sine Curve**
   - Calculate ∫sin(x) dx from 0 to π
   - Compare with exact value (2)
   - Uses n = 6 intervals

3. **Exponential Function Integration**
   - Calculate ∫e^x dx from 0 to 1
   - Compare with exact value (e - 1)
   - Allows user input for number of intervals
   - Shows accuracy changes with different n values

4. **Volume of Sphere**
   - Calculate volume of unit sphere using ∫π(1-x²) dx from -1 to 1
   - Compare with exact value (4π/3)
   - Uses n = 8 intervals

5. **Work Done by Force**
   - Calculate work done by force F(x) = 2x + 3 from x = 0 to x = 5
   - Compare with exact value (40)
   - Uses n = 10 intervals

6. **Center of Mass**
   - Find center of mass of rod with density ρ(x) = 1 + x² from x = 0 to x = 2
   - Compare with exact value (1.5)
   - Uses n = 6 intervals

7. **Arc Length**
   - Calculate arc length of y = x² from x = 0 to x = 1
   - Uses formula ∫√(1 + (dy/dx)²) dx
   - Compare with exact value (≈1.4789428575445974)
   - Uses n = 8 intervals

8. **Average Value**
   - Find average value of cos(x) over [0, π/2]
   - Compare with exact value (2/π)
   - Uses n = 4 intervals

9. **Moment of Inertia**
   - Calculate moment of inertia of rod with density ρ(x) = x² from x = 0 to x = 1
   - Compare with exact value (1/6)
   - Uses n = 6 intervals

10. **Area Between Curves**
    - Find area between y = x² and y = x³ from x = 0 to x = 1
    - Compare with exact value (1/12)
    - Uses n = 8 intervals

## Implementation Details

Each problem is implemented in both Java and Python with the following features:

- Simpson's 1/3 Rule implementation
- Input validation
- Error handling
- Comparison with exact values
- Accuracy analysis with different n values
- Clear output formatting
- Detailed comments explaining mathematical concepts

## Running the Code

### Java
```bash
cd java_solutions
javac Problem*.java
java Problem1  # Replace with problem number
```

### Python
```bash
cd python_solutions
python problem1.py  # Replace with problem number
```

## Requirements

- Java 8 or higher
- Python 3.x
- NumPy library for Python solutions

## Note

All problems use even number of intervals as required by Simpson's 1/3 Rule. The code includes error handling for invalid inputs and provides detailed output including absolute and relative errors. 