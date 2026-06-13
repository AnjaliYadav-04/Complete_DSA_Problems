import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [float('inf')] * n
dist[0] = 0

pq = [(0, 0)]

while pq:
    d, node = heapq.heappop(pq)

    for nei, w in graph[node]:
        if d + w < dist[nei]:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

print(dist[n-1])
