n = int(input())
nums = list(map(int, input().split()))
nums.sort()
min_sum = 10 ** 9 * 2

for i in range(n):
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        cur_sum = nums[i] + nums[mid]

        if cur_sum == 0:
            min_pair = (i, mid)
            break
        elif cur_sum > 0:
            end = mid - 1
        else:
            start = mid + 1

        if abs(cur_sum) < min_sum:
            min_sum = abs(cur_sum)
            min_pair = (i, mid)

for idx in min_pair:
    print(nums[idx], end=" ")