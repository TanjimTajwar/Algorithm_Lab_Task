package Max_Flow;

import java.util.*; // Import required libraries

public class findMaximumFlow {
    private static final int INF = Integer.MAX_VALUE; // Define infinity as the maximum integer value
    private int vertices; // Number of vertices in the graph
    private int[][] capacity; // Adjacency matrix for storing capacities
    private int[] parent; // Array to store the path found by BFS

    // Constructor to initialize graph with given number of vertices
    public findMaximumFlow(int vertices) {
        this.vertices = vertices;
        capacity = new int[vertices][vertices]; // Initialize capacity matrix
        parent = new int[vertices]; // Initialize parent array
    }

    // Method to add an edge with a specific capacity between two nodes
    public void addEdge(int u, int v, int cap) {
        capacity[u][v] = cap; // Set capacity from node u to v
    }

    // BFS function to find an augmenting path from source to sink
    private boolean bfs(int source, int sink) {
        boolean[] visited = new boolean[vertices]; // Array to track visited nodes
        Arrays.fill(visited, false); // Initialize visited array to false
        Queue<Integer> queue = new LinkedList<>(); // Queue for BFS traversal
        queue.add(source); // Start BFS from the source node
        visited[source] = true; // Mark source as visited
        parent[source] = -1; // Set parent of source to -1

        // Perform BFS
        while (!queue.isEmpty()) {
            int u = queue.poll(); // Get the front node from the queue
            
            for (int v = 0; v < vertices; v++) { // Check all adjacent vertices
                if (!visited[v] && capacity[u][v] > 0) { // If there is available capacity and not visited
                    queue.add(v); // Add vertex to the queue
                    parent[v] = u; // Store the parent of v
                    visited[v] = true; // Mark v as visited
                    if (v == sink) return true; // If sink is reached, return true
                }
            }
        }
        return false; // No augmenting path found
    }

    // Edmonds-Karp algorithm to find the maximum flow
    public int edmondsKarp(int source, int sink) {
        int maxFlow = 0; // Initialize maximum flow to zero

        // Augment the flow while there is a path from source to sink
        while (bfs(source, sink)) {
            int pathFlow = INF; // Start with an infinitely large flow
            
            // Find the minimum residual capacity in the augmenting path
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v]; // Get parent node
                pathFlow = Math.min(pathFlow, capacity[u][v]); // Find the minimum capacity in the path
            }

            // Update the residual capacities of the edges and reverse edges
            for (int v = sink; v != source; v = parent[v]) {
                int u = parent[v]; // Get parent node
                capacity[u][v] -= pathFlow; // Reduce forward edge capacity
                capacity[v][u] += pathFlow; // Increase reverse edge capacity
            }

            maxFlow += pathFlow; // Add path flow to total max flow
        }
        return maxFlow; // Return the total maximum flow
    }

    public static void main(String[] args) {
        int vertices = 4; // Number of vertices in the graph
        MaxFlow graph = new MaxFlow(vertices); // Create a MaxFlow object

        // Add edges with their capacities
        graph.addEdge(0, 1, 3);
        graph.addEdge(0, 2, 2);
        graph.addEdge(1, 2, 1);
        graph.addEdge(1, 3, 2);
        graph.addEdge(2, 3, 4);

        int source = 0; // Define the source node
        int sink = 3; // Define the sink node
        
        // Compute and print the maximum possible flow
        System.out.println("The maximum possible flow is: " + graph.edmondsKarp(source, sink));
    }
}
