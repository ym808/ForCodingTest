T = int(input())

for ts in range(1, T+1):
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(input().split())
    
    print(f"#{ts} ")
    for i in range(N):
        rot90, rot180, rot270 = '', '', ''
        for j in range(N):
            rot90 += grid[N-1-j][i]
            rot180 += grid[N-1-i][N-1-j]
            rot270 += grid[j][N-1-i]

        print(rot90, rot180, rot270)