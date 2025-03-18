#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int src, dest, wt;
    Edge(int s, int d, int w) : src(s), dest(d), wt(w) {}
};

class Test {
private:
    static void createGraph(vector<vector<Edge>>& graph) {
        graph[0].push_back(Edge(0, 1, 1));

        graph[1].push_back(Edge(1, 2, 1));
        graph[1].push_back(Edge(1, 0, 1));

        graph[2].push_back(Edge(2, 1, 1));
        graph[2].push_back(Edge(2, 6, 1));
        graph[2].push_back(Edge(2, 5, 1));
        graph[2].push_back(Edge(2, 4, 1));

        graph[4].push_back(Edge(4, 2, 1));
        graph[4].push_back(Edge(4, 8, 1));

        graph[5].push_back(Edge(5, 2, 1));
        graph[5].push_back(Edge(5, 8, 1));

        graph[6].push_back(Edge(6, 2, 1));
        graph[6].push_back(Edge(6, 7, 1));

        graph[7].push_back(Edge(7, 6, 1));

        graph[8].push_back(Edge(8, 4, 1));
        graph[8].push_back(Edge(8, 5, 1));
    }

    static void bfs(const vector<vector<Edge>>& graph, int v) {
        vector<bool> verified(v, false);
        queue<int> q;

        q.push(0);
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (!verified[curr]) {
                cout << curr << " ";
                verified[curr] = true;
                for (const Edge& e : graph[curr]) {
                    q.push(e.dest);
                }
            }
        }
        cout << endl;
    }

public:
    static void run() {
        int v = 9;
        vector<vector<Edge>> graph(v);
        createGraph(graph);
        bfs(graph, v);
    }
};

int main() {
    Test::run();
    return 0;
} 