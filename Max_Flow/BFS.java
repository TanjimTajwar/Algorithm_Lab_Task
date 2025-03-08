package Max_Flow;


import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BFS {
    public static void main(String[] CSECU) {
        Scanner Arnab = new Scanner(System.in);
        Arnab.close();
        int v = 7;
        ArrayList<Edge> graph[] =new  ArrayList[v];

        createGraph(graph);
        bfs(graph,v);
    }
    static class Edge{
        int src,dest,wt;
        public Edge(int s,int d,int w){
            this.src=s;
            this.dest = d;
            this.wt= w;
        }
    }
    static void createGraph(ArrayList<Edge> graph[]){
        for(int a=0;a<graph.length;a++){
            graph[a]= new ArrayList<>();
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
    public static void bfs(ArrayList<Edge> graph[],int v){
        boolean visited[] = new boolean[v];
        Queue<Integer> q = new LinkedList<>();

        q.add(0);

        while(!q.isEmpty()){
            int curr = q.remove();
            if(!visited[curr]){
                System.out.print(curr+" ");
                visited[curr]= true;

                for(int a=0;a<graph[curr].size();a++){
                    Edge e= graph[curr].get(a);
                    q.add(e.dest);
                }
            }
        }
        System.out.println();
    }
}
