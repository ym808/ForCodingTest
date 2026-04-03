from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
for _ in range(m):
    node, dest = map(int, input().split())

    graph[node].append(dest)


q = deque()
q.append(x)
distance[x] = 0

while q:
    cur_node = q.popleft()

    for next_node in graph[cur_node]:
        if distance[next_node] == -1:
            distance[next_node] = distance[cur_node] + 1
            q.append(next_node)

result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)