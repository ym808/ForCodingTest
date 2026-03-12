def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
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

cycle = False
for _ in range(e):
    a, b = map(int, input().split())

    if find_parent(a) == find_parent(b):
        cycle = True
        break

    union_parent(a,b)

if cycle == True:
    print("There's cycle")
else:
    print("There's no cycle")