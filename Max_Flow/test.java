package Max_Flow;

import java.util.*;

public class test {
    static class Edge {
        int src, dest, wt;

        public Edge(int s, int d, int w) {
            this.src = s;
            this.dest = d;
            this.wt = w;
        }
    }

    public static void main(String[] CSECU) {
        int v = 9;

        ArrayList<Edge> graph[] = new ArrayList[v];

        createGraph(graph);
        bfs(graph, v);
    }

    public static void createGraph(ArrayList<Edge> graph[]) {
        for (int a = 0; a < graph.length; a++) {
            graph[a] = new ArrayList<>();
        }

        graph[0].add(new Edge(0, 1, 1));

        graph[1].add(new Edge(1, 2, 1));
        graph[1].add(new Edge(1, 0, 1));

        graph[2].add(new Edge(2, 1, 1));
        graph[2].add(new Edge(2, 6, 1));
        graph[2].add(new Edge(2, 5, 1));
        graph[2].add(new Edge(2, 4, 1));

        graph[4].add(new Edge(4, 2, 1));
        graph[4].add(new Edge(4, 8, 1)); 

        graph[5].add(new Edge(5, 2, 1));
        graph[5].add(new Edge(5, 8, 1));

        graph[6].add(new Edge(6, 2, 1));
        graph[6].add(new Edge(6, 7, 1));

        graph[7].add(new Edge(7, 6, 1));

        graph[8].add(new Edge(8, 4, 1)); 
        graph[8].add(new Edge(8, 5, 1));
    }

    public static void bfs(ArrayList<Edge> graph[], int v) {
        boolean[] verified = new boolean[v];
        Queue<Integer> q = new LinkedList<>();

        q.add(0);
        while (!q.isEmpty()) {
            int curr = q.remove();
            if (!verified[curr]) {
                System.out.print(curr + " ");
                verified[curr] = true;
                for (int a = 0; a < graph[curr].size(); a++) {
                    Edge e = graph[curr].get(a);
                    q.add(e.dest);
                }
            }
        }
        System.out.println();
    }
}
