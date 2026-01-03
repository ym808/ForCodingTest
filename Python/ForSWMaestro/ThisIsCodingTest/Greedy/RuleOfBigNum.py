N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first = nums[-1]
second = nums[-2]

repeat = 1
sum = 0

for _ in range(M):
    if repeat > K:
        sum += second
        repeat = 1
    else:
        sum += first
        repeat += 1
print(sum)
        