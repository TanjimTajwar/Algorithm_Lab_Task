#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int src, dest, wt;
    Edge(int s, int d, int w) : src(s), dest(d), wt(w) {}
};

class BFS {
private:
    static void createGraph(vector<vector<Edge>>& graph) {
        graph[0].push_back(Edge(0, 1, 1));
        graph[0].push_back(Edge(0, 2, 1));

        graph[1].push_back(Edge(1, 0, 1));
        graph[1].push_back(Edge(1, 3, 1));

        graph[2].push_back(Edge(2, 0, 1));
        graph[2].push_back(Edge(2, 4, 1));

        graph[3].push_back(Edge(3, 1, 1));
        graph[3].push_back(Edge(3, 4, 1));
        graph[3].push_back(Edge(3, 6, 1));

        graph[4].push_back(Edge(4, 2, 1));
        graph[4].push_back(Edge(4, 3, 1));
        graph[4].push_back(Edge(4, 5, 1));

        graph[5].push_back(Edge(5, 3, 1));
        graph[5].push_back(Edge(5, 4, 1));
        graph[5].push_back(Edge(5, 6, 1));

        graph[6].push_back(Edge(6, 5, 1));
    }

    static void bfs(const vector<vector<Edge>>& graph, int v) {
        vector<bool> visited(v, false);
        queue<int> q;

        q.push(0);

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (!visited[curr]) {
                cout << curr << " ";
                visited[curr] = true;

                for (const Edge& e : graph[curr]) {
                    q.push(e.dest);
                }
            }
        }
        cout << endl;
    }

public:
    static void run() {
        int v = 7;
        vector<vector<Edge>> graph(v);
        createGraph(graph);
        bfs(graph, v);
    }
};

int main() {
    BFS::run();
    return 0;
} 