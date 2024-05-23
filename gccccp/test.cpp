#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>

using namespace std;

// 定义图的数据结构
class Graph {
public:
    Graph(int V) : V(V), adjList(V) {}

    // 添加边
    void addEdge(int v, int w) {
        adjList[v].push_back(w);
    }

    // 深度优先搜索算法
    bool DFS(int start, int target) {
        vector<bool> visited(V, false); // 记录节点是否被访问过
        stack<int> stack; // 使用栈来保存遍历过程中的节点

        stack.push(start);
        visited[start] = true;

        while (!stack.empty()) {
            int current = stack.top();
            cout<<current<<endl;
            stack.pop();

            if (current == target) {
                return true; // 找到目标节点
            }

            // 遍历当前节点的邻居节点
            for (int neighbor : adjList[current]) {
                if (!visited[neighbor]) {
                    stack.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }

        return false; // 未找到目标节点
    }

private:
    int V; // 节点数量
    vector<vector<int>> adjList; // 邻接表表示的图
};

int main() {
    Graph g(6); // 创建一个有6个节点的图

    // 添加图中的边
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(2, 5);

    int start = 3; // 起始节点
    int target = 5; // 目标节点

    if (g.DFS(start, target)) {
        cout << "Path from " << start << " to " << target << " exists." << endl;
    } else {
        cout << "Path from " << start << " to " << target << " does not exist." << endl;
    }

    system("pause");
    return 0;
}


