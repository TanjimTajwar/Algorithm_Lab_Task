public class Problem5 {
    public static void main(String[] args) {
        System.out.println("Problem 5:");
        double[][] matrix = {
            {3, 2, -1, 10},
            {2, -2, 4, -2},
            {-1, 0.5, -1, -1}
        };
        solveSystem(matrix);
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