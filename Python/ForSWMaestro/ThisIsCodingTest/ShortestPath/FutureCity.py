n, m = map(int, input().split())

INF = int(1e9)
matrix = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

z, y = map(int, input().split())

# 자기자신 거리는 0으로 초기화
for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j:
            matrix[i][j] = 0

# 경유 노선이 더 짧은지 확인
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

# matrix 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if matrix[i][j] == INF:
            print('INF', end=" ")
        else:
            print(f"{matrix[i][j]:3d}", end=" ")
    print()

result = matrix[1][y] + matrix[y][z]

if result >= INF:
    print(-1)
else:
    print(f"result: {result}")