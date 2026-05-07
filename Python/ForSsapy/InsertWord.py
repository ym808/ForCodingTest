T = int(input())

for ts in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = [input().split() for _ in range(N)]

    cnt = 0
    for i in range(N):
        cnt += ''.join(puzzle[i]).split('0').count('1'*K)
        cnt += ''.join(puzzle[j][i] for j in range(N)).split('0').count('1'*K)

    print(f"#{ts} {cnt}")