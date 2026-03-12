def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

for i in range(1, v+1):
    print(find_parent(i), end=" ")
print()

for i in range(1, v+1):
    print(parent[i], end=" ")
    