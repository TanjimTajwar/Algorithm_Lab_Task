#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Edge {
    int src, dest, weight;
    Edge(int s, int d, int w) : src(s), dest(d), weight(w) {}
};

class AllPathsSrcToDest {
private:
    static const int target = 4;
    vector<vector<Edge>> graph;
    vector<bool> visited;

    void createGraph() {
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

    void findAllPaths(int curr, string path) {
        if (curr == target) {
            cout << path << endl;
            return;
        }
        visited[curr] = true;
        for (const Edge& e : graph[curr]) {
            if (!visited[e.dest]) {
                findAllPaths(e.dest, path + "->" + to_string(e.dest));
            }
        }
        visited[curr] = false;
    }

public:
    AllPathsSrcToDest(int v) {
        graph.resize(v);
        visited.resize(v, false);
        createGraph();
    }

    void findPaths() {
        findAllPaths(0, "0");
    }
};

int main() {
    int v = 7;
    AllPathsSrcToDest graph(v);
    graph.findPaths();
    return 0;
} 