T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    prefix = [[0] * (N+1) for _ in range(N+1)]
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    max_killed_flies = 0
    for i in range(M, N+1):
        for j in range(M, N+1):
            killed_flies = prefix[i][j] - prefix[i-M][j] - prefix[i][j-M] + prefix[i-M][j-M]
            max_killed_flies = max(max_killed_flies, killed_flies)

    print(f"#{test_case} {max_killed_flies}")