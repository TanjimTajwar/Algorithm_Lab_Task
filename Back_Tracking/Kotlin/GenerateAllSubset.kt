import java.util.Scanner

// Function to generate all subsets recursively
fun generateSubset(arr: IntArray, index: Int, temp: MutableList<Int>, result: MutableList<List<Int>>) {
    // Base case: when we've processed all elements
    if (index == arr.size) {
        result.add(ArrayList(temp))
        return
    }
    
    // Exclude current element
    generateSubset(arr, index + 1, temp, result)
    
    // Include current element
    temp.add(arr[index])
    generateSubset(arr, index + 1, temp, result)
    temp.removeAt(temp.size - 1)  // Backtrack
}

fun main() {
    // Create Scanner object for input
    val scanner = Scanner(System.`in`)
    
    // Prompt user for input size
    print("Enter the number of element in the set: ")
    val n = scanner.nextInt()
    
    // Input array
    val arr = IntArray(n)
    print("Enter the elements: ")
    for (i in 0 until n) {
        arr[i] = scanner.nextInt()
    }
    
    // List to store all subsets
    val result = mutableListOf<List<Int>>()
    val temp = mutableListOf<Int>()
    
    // Generate all subsets
    generateSubset(arr, 0, temp, result)
    
    // Print all subsets
    println("So the SubSet are: ")
    println(result)
    
    // Close the scanner
    scanner.close()
} 