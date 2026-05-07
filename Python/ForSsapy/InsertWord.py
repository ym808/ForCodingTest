T = int(input())

for ts in range(1, T+1):
    N, K = map(int, input().split())

    grid = []

    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    cnt = 0
    for r in range(N):
        length = 0
        for c in range(N):
            if grid[r][c] == 1:
                length += 1
            else:
                if length == K: 
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    for c in range(N):
        length = 0
        for r in range(N):
            if grid[r][c] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    print(f"#{ts} {cnt}")