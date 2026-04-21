T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir = 0
    x, y = 0, 0
    for i in range(1, N * N + 1):
       matrix[x][y] = i

       nx = x + dx[dir]
       ny = y + dy[dir]

       if ny >= N or nx >= N or ny < 0 or matrix[nx][ny] != 0:
           dir += 1
           if dir > 3:
               dir = 0
           
           nx = x + dx[dir]
           ny = y + dy[dir]
        
       x, y = nx, ny

    print(f"#{test_case}")
    for row in matrix:
        for num in row:
            print(f"{num:<3}", end=" ")
        print()