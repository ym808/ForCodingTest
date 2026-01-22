# My code

import sys

n, x = map(int, input().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

def binarySearch(array, x, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1

start = 0
end = len(nums) - 1
x_idx = binarySearch(nums, x, start, end)
if x_idx == -1:
    x_num = x_idx
else:
    left_end = x_idx - 1
    right_start = x_idx + 1
    left_result = -1
    right_result = -1

    while left_end >= 0:
        left_x_idx = binarySearch(nums, x, start, left_end)
        if left_x_idx == -1: break
        left_end = left_x_idx - 1
        left_result = left_x_idx    

    while right_start <= end:
        right_x_idx = binarySearch(nums, x, right_start, end)
        if right_x_idx == -1: break
        right_start = right_x_idx + 1
        right_result = right_x_idx

    if right_result == -1:
        right_result = x_idx
    if left_result == -1:
        left_result = x_idx

    x_num = right_result - left_result + 1

print(x_num)
    
# Optimization Code

def find_first_x(array, x):
    start = 0
    end = len(array) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == x:
            result = mid
            end = mid - 1
        elif array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return result

def find_last_x(array, x):
    start = 0
    end = len(array) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == x:
            result = mid
            start = mid + 1
        elif array[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return result

first_x = find_first_x(nums, x)
last_x = find_last_x(nums, x)

if first_x == -1:
    print(-1)
else:
    print(last_x - first_x + 1)