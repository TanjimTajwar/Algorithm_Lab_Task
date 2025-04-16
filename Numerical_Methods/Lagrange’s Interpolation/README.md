# Lagrange Interpolation Implementation

This project contains Java implementations of various Lagrange interpolation problems.

## Files Description

1. `Problem14.java` - Basic Lagrange interpolation with 3 points
2. `Problem15.java` - General Lagrange interpolation for any number of points
3. `Problem16.java` - Displays polynomial expression
4. `Problem17.java` - High-degree polynomial interpolation with 6 points
5. `Problem18.java` - Temperature data interpolation
6. `Problem19.java` - Comparison between Lagrange and Newton interpolation
7. `Problem20.java` - Symbolic Lagrange formula display

## How to Run

1. Compile the Java files:
```bash
javac *.java
```

2. Run any problem:
```bash
java Problem14
java Problem15
# etc...
```

## Input Format

For most problems, you will need to provide:
1. Number of points
2. x values
3. y values
4. Target x value for interpolation

## Example

For Problem 14 (Basic Lagrange Interpolation):
```
x: 1 2 4
y: 1 4 16
Estimate y at x = 3
Expected Output: 9.0
```

## Notes

- All implementations use double precision for calculations
- The code includes error handling for basic cases
- Performance measurements are included where relevant
- The symbolic formula display shows the exact mathematical expression 