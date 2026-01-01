constraints = input()
nums = input()

constraints = [int(x) for x in constraints.split()]
N = constraints[0]
M = constraints[1]
K = constraints[2]

nums = [int(x) for x in nums.split()]

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
        