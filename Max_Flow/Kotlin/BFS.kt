package Max_Flow

import java.util.*

class BFS {
    data class Edge(val src: Int, val dest: Int, val wt: Int)

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val v = 7
            val graph = Array<ArrayList<Edge>>(v) { ArrayList() }
            createGraph(graph)
            bfs(graph, v)
        }

        private fun createGraph(graph: Array<ArrayList<Edge>>) {
            graph[0].add(Edge(0, 1, 1))
            graph[0].add(Edge(0, 2, 1))

            graph[1].add(Edge(1, 0, 1))
            graph[1].add(Edge(1, 3, 1))

            graph[2].add(Edge(2, 0, 1))
            graph[2].add(Edge(2, 4, 1))

            graph[3].add(Edge(3, 1, 1))
            graph[3].add(Edge(3, 4, 1))
            graph[3].add(Edge(3, 6, 1))

            graph[4].add(Edge(4, 2, 1))
            graph[4].add(Edge(4, 3, 1))
            graph[4].add(Edge(4, 5, 1))

            graph[5].add(Edge(5, 3, 1))
            graph[5].add(Edge(5, 4, 1))
            graph[5].add(Edge(5, 6, 1))

            graph[6].add(Edge(6, 5, 1))
        }

        private fun bfs(graph: Array<ArrayList<Edge>>, v: Int) {
            val visited = BooleanArray(v)
            val q: Queue<Int> = LinkedList()

            q.add(0)

            while (q.isNotEmpty()) {
                val curr = q.remove()
                if (!visited[curr]) {
                    print("$curr ")
                    visited[curr] = true

                    for (e in graph[curr]) {
                        q.add(e.dest)
                    }
                }
            }
            println()
        }
    }
} 