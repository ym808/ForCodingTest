N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

max = 0
sec_max = 0

for num in nums:
    if num > max:
        sec_max = max
        max = num

repeat = 1
sum = 0
for _ in range(M):
    if repeat > K:
        sum += sec_max
        repeat = 1
    else:
        sum += max
        repeat += 1
print(sum)
        