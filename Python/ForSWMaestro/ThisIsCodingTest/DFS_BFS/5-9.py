from collections import deque

visited = [False] * 9
graph = []

def bfs(graph, start, visited): 
    q = deque([start])

    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] == True



