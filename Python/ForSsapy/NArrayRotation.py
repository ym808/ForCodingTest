import copy
T = 1 #int(input())

for ts in range(1, T+1):
    N = int(input())
    grid = []
    rotated_grids = []
    for _ in range(N):
        row = input().split()
        grid.append(row)
    
    for _ in range(3):
        rotated_grid = [[] for _ in range(N)]
        for r in range(N-1, -1, -1):
            for i in range(N):
                rotated_grid[i].append(grid[r][i])

        rotated_grids.append(rotated_grid)
        grid = copy.deepcopy(rotated_grid)

    print(f"#{ts}")
    for r in range(N):
        for i in range(3):
            for c in range(N):
                print(rotated_grids[i][r][c], end="")
            print(end=" ")
        print()