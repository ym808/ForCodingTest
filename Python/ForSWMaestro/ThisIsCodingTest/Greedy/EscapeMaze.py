from collections import deque
row, col = map(int, input().split())
maze = []

for _ in range(row):
    maze.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):

    queue = deque([(x,y)])

    while queue:

        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= row or ny <= -1 or ny >= col: continue

            if maze[nx][ny] == 0: continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

bfs(0,0)
print(maze[row-1][col-1])
    