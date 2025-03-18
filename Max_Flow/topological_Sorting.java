package Max_Flow;
import java.util.*;

public class topological_Sorting {
    public static ArrayList<Edge> graph[];
    public static boolean vis[];
    public static int inDegree[];
    public static ArrayList<Integer> path;
    public static int count;

    static class Edge{
        int src;
        int dest;
        public Edge(int src,int dest){
            this.src=src;
            this.dest=dest;
        }
    }
    
    public static void createGraph(){
        for(int a=0;a<graph.length;a++){
            graph[a]= new ArrayList<>();
        }

        graph[5].add(new Edge(5,0));
        graph[5].add(new Edge(5,2));

        graph[2].add(new Edge(2,3));

        graph[4].add(new Edge(4,0));
        graph[4].add(new Edge(4,1));

        graph[3].add(new Edge(3,1));
    }

    public static void calculateInDegree() {
        for(int i = 0; i < graph.length; i++) {
            for(Edge e : graph[i]) {
                inDegree[e.dest]++;
            }
        }
    }
    
    public static void findAllTopologicalSorts() {
        boolean flag = false;
        
        for(int i = 0; i < graph.length; i++) {
            if(inDegree[i] == 0 && !vis[i]) {
                vis[i] = true;
                path.add(i);
                
                // Reduce in-degree for all adjacent vertices
                for(Edge e : graph[i]) {
                    inDegree[e.dest]--;
                }
                
                findAllTopologicalSorts();
                
                // Backtrack
                vis[i] = false;
                path.remove(path.size() - 1);
                for(Edge e : graph[i]) {
                    inDegree[e.dest]++;
                }
                
                flag = true;
            }
        }
        
        if(!flag) {
            count++;
            System.out.println("Topological Sort " + count + ": " + path);
        }
    }
    
    public static void main(String[] CSECU){
        int v = 6;
        /*
         5----->0<-----4
         |             |
         v             v
         2----->3----->1
         */
        graph = new ArrayList[v];
        vis = new boolean[v];
        inDegree = new int[v];
        path = new ArrayList<>();
        count = 0;
        
        createGraph();
        calculateInDegree();
        
        System.out.println("All possible topological sorts:");
        findAllTopologicalSorts();
        System.out.println("Total number of topological sorts: " + count);
    }
}