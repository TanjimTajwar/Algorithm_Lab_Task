package Max_Flow

import java.util.*

class CycleDetection {
    data class Edge(val src: Int, val dest: Int, val weight: Int)

    companion object {
        private lateinit var graph: Array<ArrayList<Edge>>
        private lateinit var vis: BooleanArray
        private lateinit var res: BooleanArray
        private var v: Int = 0

        private fun isCycle(curr: Int): Boolean {
            vis[curr] = true
            res[curr] = true
            for (e in graph[curr]) {
                if (res[e.dest]) {
                    return true
                } else if (!vis[e.dest]) {
                    if (isCycle(e.dest)) {
                        return true
                    }
                }
            }
            res[curr] = false
            return false
        }

        private fun createGraph(graph: Array<ArrayList<Edge>>) {
            for (a in 0 until v) {
                graph[a] = ArrayList()
            }

            graph[0].add(Edge(0, 2, 1))
            graph[1].add(Edge(1, 0, 1))
            graph[2].add(Edge(2, 3, 1))
            graph[3].add(Edge(3, 0, 1))
        }

        @JvmStatic
        fun main(args: Array<String>) {
            v = 4
            graph = Array(v) { ArrayList() }
            createGraph(graph)
            /*
             1---0---3
                 /  /
                 / /
                 //
                 2
             */
            vis = BooleanArray(v)
            res = BooleanArray(v)
            for (a in 0 until v) {
                if (!vis[a]) {
                    val ans = isCycle(a)
                    if (ans) {
                        println("Cycle")
                        return
                    }
                }
            }
            println("No Cycle")
        }
    }
} 