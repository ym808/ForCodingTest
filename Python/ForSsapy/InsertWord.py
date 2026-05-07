import copy

T = int(input())

for ts in range(1, T+1):
    N, K = map(int, input().split())

    original_puzzle = []
    result = 0

    for i in range(N):
        data = list(map(int, input().split()))
        original_puzzle.append(data)

    
    puzzle = copy.deepcopy(original_puzzle)
    for r in range(N):
        for c in range(0, N - K + 1):
            if puzzle[r][c] == 0: continue
            length = 0

            for i in range(N - c):
                nc = c + i
                if puzzle[r][nc] == 0: break
                length += 1
                puzzle[r][nc] = 0
            if length == K: result += 1

    puzzle = copy.deepcopy(original_puzzle)
    for c in range(N):
        for r in range(0, N - K + 1):
            if puzzle[r][c] == 0: continue
            length = 0

            for i in range(N - r):
                nr = r + i
                if puzzle[nr][c] == 0: break
                length += 1
                puzzle[nr][c] = 0
            if length == K: result += 1
    print(f"#{ts} {result}")