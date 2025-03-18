import java.util.Scanner

// Function to print Fibonacci sequence recursively
fun findFibonacci(n: Int, a: Int, b: Int) {
    // Store current value of b
    var temp = b
    // Calculate next Fibonacci number
    var newB = a + b
    // Update a to previous b value
    var newA = temp
    
    // Base case: stop if we exceed the limit
    if (n < newA || n < newB) {
        return
    }
    
    // Print current Fibonacci number
    print("+$newB")
    // Recursive call for next number
    findFibonacci(n, newA, newB)
}

fun main() {
    // Create Scanner object for input
    val scanner = Scanner(System.`in`)
    
    // Prompt user for input
    print("Enter the Limit of fibonacci sequence: ")
    val n = scanner.nextInt()
    
    // Print initial sequence
    print("1+1")
    // Start Fibonacci sequence
    findFibonacci(n, 1, 1)
    println()
    
    // Close the scanner
    scanner.close()
} 