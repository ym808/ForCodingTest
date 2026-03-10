import heapq
INF = int(1e9)

n,m,c = map(int, input().split())
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, dest, time = map(int, input().split())
    graph[start].append((dest, time))

def advanced_dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, now = heapq.heappop(q)

        for i in graph[now]:
            cost = time + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

advanced_dijkstra(start)

cities = -1
max_time = 0
for t in distance:
    if t == INF: continue
    max_time = max(max_time, t)
    cities += 1
    
print(cities, max_time)