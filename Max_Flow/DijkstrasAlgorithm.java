package Max_Flow;
import java.util.*;


public class DijkstrasAlgorithm {
    public static ArrayList<Edge>[] graph;
    public static int v;

    static class Edge{
        int src;
        int dest;
        int weight;
        public Edge(int s,int d,int w){
            this.src=s;
            this.dest=d;
            this.weight=w;
        }
    }

    public static class Pair implements  Comparable<Pair>{ 
        int node;
        int dist;
        public Pair(int n,int dest){
            this.node=n;
            this.dist=dest;
        }
    }
    public static void dijkstras(int src){
        PriorityQueue<Pair> pq=new PriorityQueue<>((a,b)->{
            return a.dist-b.dist;
        });
        pq.add(new Pair(src,0));
        boolean visited[]=new boolean[v];
        int dist[]=new int[v];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[src]=0;
        while(!pq.isEmpty()){
            Pair p=pq.poll();
            if(visited[p.node]) continue;
            visited[p.node]=true;
            for(Edge e:graph[p.node]){
                if(!visited[e.dest] && dist[e.dest]>dist[p.node]+e.weight){
                    dist[e.dest]=dist[p.node]+e.weight;
                    pq.add(new Pair(e.dest,dist[e.dest]));
                }
            }
        }
        for(int a=0;a<v;a++){
            System.out.println("Node "+a+" has distance "+dist[a]);
        }
    }
    public static void createGraph(){
        for(int a=0;a<v;a++){
            graph[a]= new ArrayList<>();
        }
        graph[0].add(new Edge(0,1,2));
        graph[0].add(new Edge(0,2,4));

        graph[1].add(new Edge(1,2,1));
        graph[1].add(new Edge(1,3,7));

        graph[2].add(new Edge(2,4,3));
        

        graph[3].add(new Edge(3,5,1));

        graph[4].add(new Edge(4,5,5));
    }
    public static void main(String [] CSECU){
        System.out.println("Dijkstra's Algorithm");
        /*
         [0]---2--->[1]---7--->[3]---1-->[5]
          |          |                    ^
          |          |                    |
          4          |                    5
          |     1----/                    | 
          v  - /                          |
         [2]---3--->[4]--------------------

          */
        v=5;
        graph=new ArrayList[v];
        createGraph();
    }
}
