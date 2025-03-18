fun findDistinctSub(str: String): Int {
    val tree = sortedSetOf<String>()
    for (a in str.indices) {
        tree.add(str.substring(a))
    }

    var count = 1
    var text2 = tree.first()

    for (text in tree) {
        if (text != text2) {
            count++
        }
        text2 = text
    }
    return count
}

fun main() {
    println("Aloha Bro: ")
    print("Enter the String: ")
    val str = readLine() ?: ""
    println("Distinct Substrings Count: ${findDistinctSub(str)}")
} 