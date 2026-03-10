INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_distance = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < min_distance and not visited[i]:
            min_distance = distance[i]
            index = i
    
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 각 노드에 대해 한다는 게 무슨 뜻이며 왜 그렇게 하는걸까?
    for _ in range(n-1):
        now = get_smallest_node()

        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])
    

