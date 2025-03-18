fun findLSS(mystr: String, length: Int): String {
    val myTree = sortedSetOf<String>()
    for (a in 0 until length) {
        myTree.add(mystr.substring(a))
    }
    return myTree.first()
}

fun main() {
    println("Lets Code it.")
    print("Enter the String: ")
    val mystr = readLine() ?: ""
    val length = mystr.length
    println("The Lexicographically Smallest Suffix is : ${findLSS(mystr, length)}")
} 