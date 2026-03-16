def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

graph = [[] for _ in range(n+1)]
edges = []

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    edges.append((c,a,b))

edges.sort()
cost_sum = 0
max_cost = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost_sum += cost
        if cost > max_cost:
            max_cost = cost

cost_sum -= max_cost

print(cost_sum)