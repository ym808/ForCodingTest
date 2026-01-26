n = int(input())
nums = list(map(int, input().split()))

min_sum = 10 ** 9 + 1

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        cur_sum = abs(nums[i] + nums[j])
        if cur_sum <= min_sum:
            min_sum = cur_sum
            min_pair = (nums[i], nums[j])

for num in min_pair:
    print(num, end=" ")