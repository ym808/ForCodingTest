from collections import deque
import sys
INF = int(1e6)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node, dest = map(int, input().split())
    graph[node].append(dest)

distance = [INF] * (n+1)
visited = [False] * (n+1)


distance[x] = 0

def bfs():
    d = deque()
    d.append(x)

    while d:
        node = d.popleft()
        if visited[node] == True: continue
        else: visited[node] = True

        for i in graph[node]:
            d.append(i)
            
            if distance[node] + 1 < distance[i]:
                distance[i] = distance[node] + 1

bfs()
result = []
for i in range(1, len(distance)):
    if distance[i] == k:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)