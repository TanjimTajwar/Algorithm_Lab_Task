#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int src, dest, weight;
    Edge(int s, int d, int w) : src(s), dest(d), weight(w) {}
};

class CycleDetection {
private:
    vector<vector<Edge>> graph;
    vector<bool> vis;
    vector<bool> res;
    int v;

    bool isCycle(int curr) {
        vis[curr] = true;
        res[curr] = true;
        for (const Edge& e : graph[curr]) {
            if (res[e.dest]) {
                return true;
            } else if (!vis[e.dest]) {
                if (isCycle(e.dest)) {
                    return true;
                }
            }
        }
        res[curr] = false;
        return false;
    }

    void createGraph() {
        graph[0].push_back(Edge(0, 2, 1));
        graph[1].push_back(Edge(1, 0, 1));
        graph[2].push_back(Edge(2, 3, 1));
        graph[3].push_back(Edge(3, 0, 1));
    }

public:
    CycleDetection(int vertices) : v(vertices) {
        graph.resize(v);
        vis.resize(v, false);
        res.resize(v, false);
        createGraph();
    }

    bool hasCycle() {
        for (int i = 0; i < v; i++) {
            if (!vis[i]) {
                if (isCycle(i)) {
                    return true;
                }
            }
        }
        return false;
    }
};

int main() {
    int v = 4;
    CycleDetection graph(v);
    /*
     1---0---3
         /  /
         / /
         //
         2
     */
    if (graph.hasCycle()) {
        cout << "Cycle" << endl;
    } else {
        cout << "No Cycle" << endl;
    }
    return 0;
} 