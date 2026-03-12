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

for i in range(n+1):
    parent[i] = i

queries = []
for _ in range(m):
    oper, a, b = map(int, input().split())
    queries.append((oper, a, b))

for oper, a, b in queries:
    match oper:
        case 0:
            union_parent(parent, a, b)
        case 1:
            if find_parent(parent, a) == find_parent(parent, b):
                print("Yes")
            else:
                print("No")