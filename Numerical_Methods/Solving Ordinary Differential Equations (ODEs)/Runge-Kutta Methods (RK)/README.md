# Runge-Kutta Methods Implementation

This project contains implementations of various Runge-Kutta methods to solve ordinary differential equations (ODEs) in both Java and Python.

## Project Structure

```
.
├── java_solutions/
│   ├── Problem1.java
│   ├── Problem2.java
│   └── ...
├── python_solutions/
│   ├── problem1.py
│   ├── problem2.py
│   └── ...
├── runge_kutta_methods.txt
└── runge_kutta_problems.txt
```

## Requirements

### Java
- Java Development Kit (JDK) 8 or higher
- Any Java IDE or command line compiler

### Python
- Python 3.x
- NumPy library (`pip install numpy`)

## How to Run

### Java Files
1. Navigate to the java_solutions directory
2. Compile the Java file:
   ```bash
   javac Problem1.java
   ```
3. Run the compiled class:
   ```bash
   java Problem1
   ```

### Python Files
1. Navigate to the python_solutions directory
2. Run the Python file:
   ```bash
   python problem1.py
   ```

## Problem Descriptions

The problems are described in `runge_kutta_problems.txt`. Each problem includes:
- The differential equation
- Initial conditions
- Step size
- Target x value
- Method to use (RK2, RK3, or RK4)

## Method Explanations

Detailed explanations of Runge-Kutta methods, including formulas and solution steps, can be found in `runge_kutta_methods.txt`.

## Notes
- Each problem is implemented in both Java and Python
- The Python implementations use NumPy for numerical computations
- Some problems include exact solutions for error comparison
- For problems without exact solutions, the numerical solution is provided 