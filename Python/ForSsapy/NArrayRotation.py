T = int(input())

for ts in range(1, T+1):
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(input().split())
    
    print(f"#{ts} ")
    for i in range(N):
        rot90 = ''.join(grid[N-1-j][i] for j in range(N))
        rot180 = ''.join(grid[N-1-i][N-1-j] for j in range(N))
        rot270 = ''.join(grid[j][N-1-i] for j in range(N))

        print(rot90, rot180, rot270)