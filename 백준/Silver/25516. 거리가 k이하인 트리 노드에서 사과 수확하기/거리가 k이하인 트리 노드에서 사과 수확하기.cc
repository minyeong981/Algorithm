#include <iostream>
#include <vector>

using namespace std;

int n, k;
vector<vector<int>> adj;
vector<int> apple;
int ans = 0;

void dfs(int node, int dist) {
    if (dist > k) return;

    ans += apple[node];

    for (int child : adj[node]) {
        dfs(child, dist + 1);
    }
}

int main() {
    cin >> n >> k;

    adj.resize(n);
    apple.resize(n);

    for (int i = 0; i < n - 1; ++i) {
        int parent, child;
        cin >> parent >> child;
        adj[parent].push_back(child);
    }

    for (int i = 0; i < n; ++i) {
        cin >> apple[i];
    }

    dfs(0, 0);
    cout << ans << endl;

    return 0;
}
