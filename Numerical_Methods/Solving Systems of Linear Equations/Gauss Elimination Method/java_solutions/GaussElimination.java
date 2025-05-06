public class GaussElimination {
    public static void main(String[] args) {
        // Problem 1
        System.out.println("Problem 1:");
        double[][] matrix1 = {
            {2, 1, -1, 8},
            {-3, -1, 2, -11},
            {-2, 1, 2, -3}
        };
        solveSystem(matrix1);

        // Problem 2
        System.out.println("\nProblem 2:");
        double[][] matrix2 = {
            {1, 2, 3, 14},
            {2, 5, 2, 18},
            {3, 1, 5, 20}
        };
        solveSystem(matrix2);

        // Problem 3
        System.out.println("\nProblem 3:");
        double[][] matrix3 = {
            {4, 3, 2, 25},
            {-2, 2, 3, -10},
            {3, -5, 2, -4}
        };
        solveSystem(matrix3);

        // Problem 4
        System.out.println("\nProblem 4:");
        double[][] matrix4 = {
            {2, -1, 3, 9},
            {1, 1, 1, 6},
            {1, -1, 1, 2}
        };
        solveSystem(matrix4);

        // Problem 5
        System.out.println("\nProblem 5:");
        double[][] matrix5 = {
            {3, 2, -1, 10},
            {2, -2, 4, -2},
            {-1, 0.5, -1, -1}
        };
        solveSystem(matrix5);

        // Problem 6
        System.out.println("\nProblem 6:");
        double[][] matrix6 = {
            {1, 1, 1, 6},
            {2, 3, 4, 20},
            {3, 4, 5, 30}
        };
        solveSystem(matrix6);

        // Problem 7
        System.out.println("\nProblem 7:");
        double[][] matrix7 = {
            {2, 3, -1, 5},
            {4, 4, -3, 3},
            {-2, 3, -1, 1}
        };
        solveSystem(matrix7);

        // Problem 8
        System.out.println("\nProblem 8:");
        double[][] matrix8 = {
            {1, 2, 3, 6},
            {2, 5, 2, 4},
            {6, -3, 1, 2}
        };
        solveSystem(matrix8);

        // Problem 9
        System.out.println("\nProblem 9:");
        double[][] matrix9 = {
            {2, -1, 3, 9},
            {3, 1, 2, 11},
            {1, -3, 2, 5}
        };
        solveSystem(matrix9);

        // Problem 10
        System.out.println("\nProblem 10:");
        double[][] matrix10 = {
            {1, 1, 1, 3},
            {2, 3, 1, 6},
            {3, 5, 2, 11}
        };
        solveSystem(matrix10);
    }

    public static void solveSystem(double[][] matrix) {
        int n = matrix.length;
        
        // Forward elimination
        for (int i = 0; i < n; i++) {
            // Find pivot
            int maxRow = i;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(matrix[j][i]) > Math.abs(matrix[maxRow][i])) {
                    maxRow = j;
                }
            }

            // Swap rows
            double[] temp = matrix[i];
            matrix[i] = matrix[maxRow];
            matrix[maxRow] = temp;

            // Eliminate
            for (int j = i + 1; j < n; j++) {
                double factor = matrix[j][i] / matrix[i][i];
                for (int k = i; k <= n; k++) {
                    matrix[j][k] -= factor * matrix[i][k];
                }
            }
        }

        // Back substitution
        double[] solution = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += matrix[i][j] * solution[j];
            }
            solution[i] = (matrix[i][n] - sum) / matrix[i][i];
        }

        // Print solution
        System.out.println("Solution:");
        for (int i = 0; i < n; i++) {
            System.out.printf("x%d = %.4f\n", i + 1, solution[i]);
        }
    }
} 