#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class FindMaximumFlow {
private:
    int vertices;
    vector<vector<int>> capacity;
    vector<int> parent;

public:
    FindMaximumFlow(int v) : vertices(v) {
        capacity.resize(v, vector<int>(v, 0));
        parent.resize(v);
    }

    void addEdge(int u, int v, int cap) {
        capacity[u][v] = cap;
    }

    bool bfs(int source, int sink) {
        vector<bool> visited(vertices, false);
        queue<int> q;
        q.push(source);
        visited[source] = true;
        parent[source] = -1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            
            for (int v = 0; v < vertices; v++) {
                if (!visited[v] && capacity[u][v] > 0) {
                    q.push(v);
                    parent[v] = u;
                    visited[v] = true;
                    if (v == sink) return true;
                }
            }
        }
        return false;
    }

    int edmondsKarp(int source, int sink) {
        int maxFlow = 0;
        const int INF = INT_MAX;

        while (bfs(source, sink)) {
            int pathFlow = INF;
            
            int v = sink;
            while (v != source) {
                int u = parent[v];
                pathFlow = min(pathFlow, capacity[u][v]);
                v = parent[v];
            }

            v = sink;
            while (v != source) {
                int u = parent[v];
                capacity[u][v] -= pathFlow;
                capacity[v][u] += pathFlow;
                v = parent[v];
            }

            maxFlow += pathFlow;
        }
        return maxFlow;
    }
};

int main() {
    int vertices = 4;
    FindMaximumFlow graph(vertices);

    graph.addEdge(0, 1, 3);
    graph.addEdge(0, 2, 2);
    graph.addEdge(1, 2, 1);
    graph.addEdge(1, 3, 2);
    graph.addEdge(2, 3, 4);

    int source = 0;
    int sink = 3;
    
    cout << "The maximum possible flow is: " << graph.edmondsKarp(source, sink) << endl;
    return 0;
} 