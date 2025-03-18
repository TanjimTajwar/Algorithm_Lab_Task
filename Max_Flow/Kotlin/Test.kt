package Max_Flow

import java.util.*

class Test {
    data class Edge(val src: Int, val dest: Int, val wt: Int)

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val v = 9
            val graph = Array<ArrayList<Edge>>(v) { ArrayList() }
            createGraph(graph)
            bfs(graph, v)
        }

        private fun createGraph(graph: Array<ArrayList<Edge>>) {
            graph[0].add(Edge(0, 1, 1))

            graph[1].add(Edge(1, 2, 1))
            graph[1].add(Edge(1, 0, 1))

            graph[2].add(Edge(2, 1, 1))
            graph[2].add(Edge(2, 6, 1))
            graph[2].add(Edge(2, 5, 1))
            graph[2].add(Edge(2, 4, 1))

            graph[4].add(Edge(4, 2, 1))
            graph[4].add(Edge(4, 8, 1))

            graph[5].add(Edge(5, 2, 1))
            graph[5].add(Edge(5, 8, 1))

            graph[6].add(Edge(6, 2, 1))
            graph[6].add(Edge(6, 7, 1))

            graph[7].add(Edge(7, 6, 1))

            graph[8].add(Edge(8, 4, 1))
            graph[8].add(Edge(8, 5, 1))
        }

        private fun bfs(graph: Array<ArrayList<Edge>>, v: Int) {
            val verified = BooleanArray(v)
            val q: Queue<Int> = LinkedList()

            q.add(0)
            while (q.isNotEmpty()) {
                val curr = q.remove()
                if (!verified[curr]) {
                    print("$curr ")
                    verified[curr] = true
                    for (e in graph[curr]) {
                        q.add(e.dest)
                    }
                }
            }
            println()
        }
    }
} 