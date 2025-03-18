import java.util.Scanner

// Global variables
val mylist = mutableListOf<List<String>>()
var str: String = ""

// Function to check if a substring is palindrome
fun isSafe(start: Int, end: Int): Boolean {
    var i = start
    var j = end
    while (i < j) {
        if (str[i++] != str[j--]) {
            return false
        }
    }
    return true
}

// Function to find all palindrome partitioning
fun findPalindromePartitioning(index: Int, temp: MutableList<String>) {
    // Base case: if we've reached the end of string
    if (index == str.length) {
        mylist.add(ArrayList(temp))
        return
    }
    
    // Try all possible partitions
    for (i in index until str.length) {
        if (isSafe(index, i)) {
            // Add current palindrome substring
            temp.add(str.substring(index, i + 1))
            // Recur for remaining string
            findPalindromePartitioning(i + 1, temp)
            // Backtrack
            temp.removeAt(temp.size - 1)
        }
    }
}

fun main() {
    val scanner = Scanner(System.`in`)
    
    print("Enter the String: ")
    str = scanner.next()
    
    val temp = mutableListOf<String>()
    findPalindromePartitioning(0, temp)
    
    println("So the Palindrome Partitioning Set is:")
    println(mylist)
    
    scanner.close()
} 