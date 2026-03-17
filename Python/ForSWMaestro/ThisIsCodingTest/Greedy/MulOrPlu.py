nums = list(map(int, list(input())))

result = 0

result += nums[0]

for num in nums[1:]:
    if result == 0:
        result += num
    elif num == 0:
        result += num
    elif num == 1:
        result += num
    else:
        result *= num

print(result)
