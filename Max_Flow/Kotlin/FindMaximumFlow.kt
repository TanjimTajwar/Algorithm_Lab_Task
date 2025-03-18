package Max_Flow

import java.util.*

class FindMaximumFlow(private val vertices: Int) {
    private val capacity: Array<IntArray> = Array(vertices) { IntArray(vertices) }
    private val parent: IntArray = IntArray(vertices)

    fun addEdge(u: Int, v: Int, cap: Int) {
        capacity[u][v] = cap
    }

    private fun bfs(source: Int, sink: Int): Boolean {
        val visited = BooleanArray(vertices)
        val queue: Queue<Int> = LinkedList()
        queue.add(source)
        visited[source] = true
        parent[source] = -1

        while (queue.isNotEmpty()) {
            val u = queue.poll()
            
            for (v in 0 until vertices) {
                if (!visited[v] && capacity[u][v] > 0) {
                    queue.add(v)
                    parent[v] = u
                    visited[v] = true
                    if (v == sink) return true
                }
            }
        }
        return false
    }

    fun edmondsKarp(source: Int, sink: Int): Int {
        var maxFlow = 0
        val INF = Int.MAX_VALUE

        while (bfs(source, sink)) {
            var pathFlow = INF
            
            var v = sink
            while (v != source) {
                val u = parent[v]
                pathFlow = minOf(pathFlow, capacity[u][v])
                v = parent[v]
            }

            v = sink
            while (v != source) {
                val u = parent[v]
                capacity[u][v] -= pathFlow
                capacity[v][u] += pathFlow
                v = parent[v]
            }

            maxFlow += pathFlow
        }
        return maxFlow
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val vertices = 4
            val graph = FindMaximumFlow(vertices)

            graph.addEdge(0, 1, 3)
            graph.addEdge(0, 2, 2)
            graph.addEdge(1, 2, 1)
            graph.addEdge(1, 3, 2)
            graph.addEdge(2, 3, 4)

            val source = 0
            val sink = 3
            
            println("The maximum possible flow is: ${graph.edmondsKarp(source, sink)}")
        }
    }
} 