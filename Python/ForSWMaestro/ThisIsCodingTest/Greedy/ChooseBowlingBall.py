n, m = map(int, input().split())
weights = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        if weights[i] == weights[j]: continue
        count += 1

print(count)