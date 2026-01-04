N, M = map(int, input().split())

matrix = []
result = 0
for n in range(N):
    matrix = list(map(int, input().split()))
    min_num = min(matrix)
    result = max(min_num, result)
print(result)
