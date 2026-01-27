n = int(input())
nums = list(map(int, input().split()))
nums.sort()
min_sum = 10 ** 9 * 2

start = 0
end = n - 1
while start < end:
    cur_sum = nums[start] + nums[end]
    
    if abs(cur_sum) < min_sum:
        min_sum = abs(cur_sum)
        min_pair = (start, end)

    if cur_sum == 0: 
        break
    elif cur_sum < 0:
        start += 1
    else:
        end -= 1

for idx in min_pair:
    print(nums[idx], end=" ")