from typing import List
import math

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        # Build graph
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = math.ceil(math.log2(n)) + 1
        parent = [[-1] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        # DFS
        def dfs(node, par):
            parent[node][0] = par
            for nei in graph[node]:
                if nei != par:
                    depth[nei] = depth[node] + 1
                    dfs(nei, node)

        dfs(1, -1)

        # Binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if parent[i][j - 1] != -1:
                    parent[i][j] = parent[parent[i][j - 1]][j - 1]

        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            # Bring u up
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            return parent[u][0]

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[ancestor]

            if path_len == 0:
                ans.append(0)
            else:
                ans.append(pow(2, path_len - 1, MOD))

        return ans
