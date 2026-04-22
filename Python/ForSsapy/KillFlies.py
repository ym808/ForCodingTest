T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    max_killed_flies = 0
    for i in range(N - M + 1):    
        for j in range(N - M + 1):    
            killed_flies = 0
            for r in range(M):
                for c in range(M):
                    killed_flies += grid[r+i][c+j]

            max_killed_flies = max(max_killed_flies, killed_flies)

    print(f"#{test_case} {max_killed_flies}")
            

