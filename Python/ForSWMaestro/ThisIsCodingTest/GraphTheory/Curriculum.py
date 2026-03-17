from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
req_time = [[0] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(1, n+1):
    query = list(map(int, input().split()))
    time[i] = query[0]
    indegree[i] = len(query) - 2
    
    for j in range(1, len(query)-1):
        graph[query[j]].append(i)


def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        time[now] += max(req_time[now])

        for neighbor in graph[now]:
            indegree[neighbor] -= 1
            req_time[neighbor].append(time[now])

            if indegree[neighbor] == 0:
                q.append(neighbor)

topology_sort()
for t in time:
    if t == 0: continue
    print(t)