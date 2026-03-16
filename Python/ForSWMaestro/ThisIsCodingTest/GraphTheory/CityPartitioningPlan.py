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

edges = []

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
cost_sum = 0
last = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost_sum += cost
        last = cost

cost_sum -= last

print(cost_sum)