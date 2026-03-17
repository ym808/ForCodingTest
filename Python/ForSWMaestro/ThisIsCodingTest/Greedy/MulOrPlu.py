nums = list(map(int, list(input())))

result = nums[0]

for num in nums[1:]:
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)