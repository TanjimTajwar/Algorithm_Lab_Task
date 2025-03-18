import java.util.Scanner

// Global variables
var target: Int = 0
val mylist = mutableListOf<List<Int>>()
var n: Int = 0

// Function to find all subsets that sum up to target
fun findSubSetSum(index: Int, temp: MutableList<Int>, arr: IntArray, remaining: Int) {
    // Base case: if we found a subset that sums to target
    if (remaining == 0) {
        mylist.add(ArrayList(temp))
        return
    }
    
    // Base case: if we've reached end of array or remaining sum is negative
    if (index == n || remaining < 0) {
        return
    }
    
    // Include current element
    temp.add(arr[index])
    findSubSetSum(index + 1, temp, arr, remaining - arr[index])
    
    // Exclude current element
    temp.removeAt(temp.size - 1)
    findSubSetSum(index + 1, temp, arr, remaining)
}

fun main() {
    val scanner = Scanner(System.`in`)
    
    print("Enter the number of elements in the set: ")
    n = scanner.nextInt()
    
    print("Enter the Set: ")
    val arr = IntArray(n)
    for (i in 0 until n) {
        arr[i] = scanner.nextInt()
    }
    
    print("Enter the Target Sum: ")
    target = scanner.nextInt()
    
    val temp = mutableListOf<Int>()
    findSubSetSum(0, temp, arr, target)
    
    println("So the sum set is:")
    println(mylist)
    
    scanner.close()
} 