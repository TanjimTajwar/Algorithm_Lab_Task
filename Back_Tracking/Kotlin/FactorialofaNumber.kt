import java.util.Scanner

// Function to calculate factorial recursively
fun findFactorial(n: Int): Long {
    // Base case: factorial of 0 or 1 is 1
    if (n == 0 || n == 1) {
        return 1
    }
    // Recursive case: n! = n * (n-1)!
    return n * findFactorial(n - 1)
}

fun main() {
    // Create Scanner object for input
    val scanner = Scanner(System.`in`)
    
    // Prompt user for input
    print("Enter the number: ")
    val n = scanner.nextInt()
    
    // Calculate and display factorial
    println("So the Factorial of $n is ${findFactorial(n)}")
    
    // Close the scanner
    scanner.close()
} 