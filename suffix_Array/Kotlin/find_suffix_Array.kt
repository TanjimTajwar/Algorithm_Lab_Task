var text: String = ""

fun find_suffix_array() {
    val n = text.length
    val myList = mutableListOf<Pair<Int, String>>()

    for (a in 0 until n) {
        myList.add(Pair(a, text.substring(a)))
    }

    // Sort the list based on suffixes
    myList.sortBy { it.second }

    // Print the sorted suffix array map
    println("Suffix Array:")
    for (answer in myList) {
        print("${answer.first} ")
    }
    println()
}

fun main() {
    text = readLine() ?: ""
    find_suffix_array()
} 