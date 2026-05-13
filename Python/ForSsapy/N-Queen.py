T = int(input())

for ts in range(1, T+1):

    N = int(input())

    used_col = [False] * N
    diag1 = [False] * (2 * N)
    diag2 = [False] * (2 * N)

    count = 0
    def backtrack(row):
        global count
        if row == N:
            count += 1
            return
        
        for col in range(N):
            if used_col[col] or diag1[col + row] or diag2[row - col + N-1]:
                continue

            used_col[col] = diag1[col + row] = diag2[row - col + N-1] = True

            backtrack(row+1)

            used_col[col] = diag1[col + row] = diag2[row - col + N-1] = False

    backtrack(0)

    print(f"#{ts} {count}")
