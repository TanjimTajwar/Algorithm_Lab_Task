package Max_Flow;

import java.util.ArrayList;

public class cycle_Detection {
    public static ArrayList<Edge> graph[];
    public static boolean vis[];
    public static boolean res[];
    
    public static boolean isCycle(int curr){
        vis[curr]=true;
        res[curr]=true;
        for(int a=0;a<graph[curr].size();a++){
            Edge e=graph[curr].get(a);
            if(res[e.dest]){
                return true;
            }
            else if(!vis[e.dest]){
                if(isCycle(e.dest)){
                    return true;
                }
            }
        }
        res[curr]=false;
        return false;
    }

    public static int v;
    static class Edge{
        int src;
        int dest;
        int weight;
        public Edge(int src, int dest, int weight){
            this.src=src;
            this.dest=dest;
            this.weight=weight;
        }
    }
    
    public static void createGraph(ArrayList<Edge> graph[]){
        for(int a=0;a<v;a++){
            graph[a]=new ArrayList<>();
        }
        
        graph[0].add(new Edge(0,2,1));
        graph[1].add(new Edge(1,0,1));
        graph[2].add(new Edge(2,3,1));
        graph[3].add(new Edge(3,0,1));
    }
    
    public static void main(String[] CSECU){
        v=4;
        graph = new ArrayList[v];
        createGraph(graph);
        /*
         1---0---3
             /  /
             / /
             //
             2
         */
        vis=new boolean[v];
        res=new boolean[v];
        for(int a=0;a<v;a++){
            if(!vis[a]){
                boolean ans=isCycle(a);
                if(ans){
                    System.out.println("Cycle");
                    return;
                }
            }
        }
        System.out.println("No Cycle");
    }
}
