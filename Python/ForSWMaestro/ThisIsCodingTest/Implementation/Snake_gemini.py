from collections import deque

n = int(input())
k = int(input())

field = [[0] * n for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1


l = int(input())
turns = {}
for _ in range(l):
    time, direct = input().split()
    turns[int(time)] = direct

snake = deque()
x, y = 0, 0
snake.append((x,y))
direction = 0
time = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    time += 1

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or field[nx][ny] == 2:
        break

    if field[nx][ny] == 1:
        field[nx][ny] == 0
    else:
        tail_x, tail_y = snake.pop()
        field[tail_x][tail_y] = 0
    
    field[nx][ny] = 2
    x, y = nx, ny
    snake.appendleft((x, y))

    if turns.get(time):
        if turns[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
    
print(time)

