N, M = map(int, input().split())

matrix = []
max = 0
for n in range(N):
    matrix = sorted(map(int, input().split()))
    if matrix[0] > max:
        max = matrix[0]
print(max)

