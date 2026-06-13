from typing import List
from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find max depth from node 1
        q = deque([(1, 0)])
        visited = set([1])
        max_depth = 0
        
        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))
        
        L = max_depth
        
        # If no edges in path
        if L == 0:
            return 0
        
        return pow(2, L - 1, MOD)
