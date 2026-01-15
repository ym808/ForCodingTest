# My code
from collections import deque

def bfs(v):
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i] and ice_map[i // col_size][i % col_size] == 0:
                queue.append(i)
                visited[i] = True

row_size, col_size = map(int, input().split())
map_size = row_size * col_size
visited = [False] * map_size
ice_map = []
graph = [[] for _ in range(row_size * col_size)]

idx = 0
for _ in range(row_size):
    cols = list(map(int, list(input())))
    ice_map.append(cols)

    for _ in range(col_size - 1):
        graph[idx].append(idx + 1)
        idx += 1
    rev_idx = idx
    for _ in range(col_size - 1):
        graph[rev_idx].append(rev_idx - 1)
        rev_idx -= 1
    idx += 1

for i in range(col_size):
    j = i
    for _ in range(row_size - 1):
        graph[j].append(j + col_size)
        j += col_size

    k = i + (row_size - 1) * col_size
    for _ in range(row_size - 1):
        graph[k].append(k - col_size)
        k -= col_size

queue = deque()
count = 0
for i in range(row_size):
    for j in range(col_size):
        if ice_map[i][j] == 0 and visited[i * col_size + j] == False:
            bfs(i * col_size + j)
            count += 1
    
print(count)

# Book Code

row, col = map(int, input().split())

graph = []
for x in range(row):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= row or y <= -1 or y >= col:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0
for x in range(row):
    for y in range(col):
        if dfs(x, y):
            count += 1

print(count)

# My code book ver.

from collections import deque

row, col = map(int, input().split())

graph = []
for _ in range(row):
        graph.append(list(map(int, input())))


def bfs(x, y):
    
    queue = deque([(x, y)])

    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]
        if x <= -1 or x >= row or y <= -1 or y >= col: continue
        
        if graph[x][y] == 0:
            graph[x][y] = 1
            
            queue.append((x+1, y))
            queue.append((x-1, y))
            queue.append((x, y+1))
            queue.append((x, y-1))
        else: continue
    return 

count = 0
for x in range(row):
    for y in range(col):
        if graph[x][y] == 0:
            bfs(x, y)
            count += 1
print(count)

    