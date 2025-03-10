package Max_Flow;

import java.util.ArrayList;

public class allPathsSrcTODest {
    static class Edge{
        int src;
        int dest; 
        int weight;
        public Edge(int src,int dest,int weight){
            this.src=src;
            this.dest=dest;
            this.weight=weight;
        }
    }

    public static ArrayList<Edge> graph[];
    public static boolean visited[];
    public static int target = 4;

    public static void main(String[] CSECU) {
        int v=7;
        graph= new ArrayList[v];
        visited=new boolean[v];
        createGraph();
        findAllPaths(0,"0");
    }

    public static void createGraph(){
        for(int a=0;a<graph.length;a++){
            graph[a]=new ArrayList<>();
        }

        graph[0].add(new Edge(0, 1, 1));
        graph[0].add(new Edge(0,2,1));

        graph[1].add(new Edge(1, 0, 1));
        graph[1].add(new Edge(1, 3, 1));

        graph[2].add(new Edge(2, 0, 1));
        graph[2].add(new Edge(2, 4, 1));

        graph[3].add(new Edge(3, 1, 1));
        graph[3].add(new Edge(3, 4, 1));
        graph[3].add(new Edge(3, 6, 1));

        graph[4].add(new Edge(4, 2, 1));
        graph[4].add(new Edge(4, 3, 1));
        graph[4].add(new Edge(4, 5, 1));

        graph[5].add(new Edge(5, 3, 1));
        graph[5].add(new Edge(5, 4, 1));
        graph[5].add(new Edge(5, 6, 1));

        graph[6].add(new Edge(6, 5, 1));
    }

    public static void findAllPaths(int curr,String path){
        if(curr==target){
            System.out.println(path);
            return;
        }
        visited[curr]=true;
        for(int a=0;a<graph[curr].size();a++){
            Edge e = graph[curr].get(a);
            if(!visited[e.dest]){
                findAllPaths(e.dest,path+"->"+e.dest);
            }
        }
        visited[curr]=false;
    }
}