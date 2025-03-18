package Max_Flow

import java.util.*

class DepthFirstSearch {
    data class Edge(val src: Int, val dest: Int, val weight: Int)

    companion object {
        private lateinit var visited: BooleanArray
        private lateinit var graph: Array<ArrayList<Edge>>

        @JvmStatic
        fun main(args: Array<String>) {
            val v = 7
            graph = Array(v) { ArrayList() }
            createGraph()
            visited = BooleanArray(v)
            for (a in 0 until v) {
                if (!visited[a]) {
                    dfs(a)
                }
            }
            println()
        }

        private fun createGraph() {
            graph[0].add(Edge(0, 1, 1))
            graph[0].add(Edge(0, 2, 1))

            graph[1].add(Edge(1, 3, 1))
            graph[1].add(Edge(1, 0, 1))

            graph[2].add(Edge(2, 4, 1))
            graph[2].add(Edge(2, 0, 1))

            graph[3].add(Edge(3, 4, 1))
            graph[3].add(Edge(3, 1, 1))
            graph[3].add(Edge(3, 5, 1))

            graph[4].add(Edge(4, 2, 1))
            graph[4].add(Edge(4, 3, 1))
            graph[4].add(Edge(4, 5, 1))

            graph[5].add(Edge(5, 3, 1))
            graph[5].add(Edge(5, 4, 1))
            graph[5].add(Edge(5, 6, 1))

            graph[6].add(Edge(6, 5, 1))
        }

        private fun dfs(curr: Int) {
            print("$curr ")
            visited[curr] = true
            for (e in graph[curr]) {
                if (!visited[e.dest]) {
                    dfs(e.dest)
                }
            }
        }
    }
} 