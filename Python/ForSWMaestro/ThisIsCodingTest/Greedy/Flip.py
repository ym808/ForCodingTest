nums = list(map(int, list(input())))

one_groups = 0
zero_groups = 0

if nums[0] == 0:
    zero_groups += 1
elif nums[0] == 1:
    one_groups += 1

prev = nums[0]


for num in nums[1:]:
    if num == prev: continue

    if num == 0:
        zero_groups += 1
    else:
        one_groups += 1
    
    prev = num

print(min(zero_groups, one_groups))