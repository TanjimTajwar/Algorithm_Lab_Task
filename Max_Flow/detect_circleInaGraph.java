package Max_Flow;
import java.util.*;

public class detect_circleInaGraph {
    public static ArrayList<Edge>[] graph;
    public static boolean visited[];
    public static int v;

    static class Edge{
        int src;
        int dest;
        public Edge(int s,int d){
            this.src=s;
            this.dest=d;
        }
    }
    
    public static void main (String CSECU[]){
        /*

         0----1---2----3
         |   /  
         |  /
         | /
         4----5

         */
        v=7;
        graph=new ArrayList[v];
        visited=new boolean[v];
        createGraph();
        for(int a=0;a<v;a++){
            if(!visited[a]){
                if(findCircle(a,-1)){
                    System.out.println("Cycle detected");
                    return;
                }
            }
        }
    }
    public static void createGraph(){
        for(int a=0;a<v;a++){
            graph[a]= new ArrayList<>();
        }
        graph[0].add(new Edge(0,1));
        graph[0].add(new Edge(0,4));

        graph[1].add(new Edge(1,0));
        graph[1].add(new Edge(1,2));
        graph[1].add(new Edge(1,4));

        graph[2].add(new Edge(2,1));
        graph[2].add(new Edge(2,3));

        graph[3].add(new Edge(3,2));

        graph[4].add(new Edge(4,0));
        graph[4].add(new Edge(4,1));
        graph[4].add(new Edge(4,5));

        graph[5].add(new Edge(5,4));
    }
    public static boolean findCircle(int curr,int par){
        visited[curr]=true;
        for(Edge e:graph[curr]){
            if(!visited[e.dest]){
                if(findCircle(e.dest, curr)){
                    return true;
                }
                else if(e.dest!=par){
                    return true;
                }
            }
        }
        return false;
    }
}
