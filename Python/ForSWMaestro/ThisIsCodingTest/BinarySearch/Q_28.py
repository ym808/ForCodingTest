import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

def find_fixedP(array):
    start = 0
    end = len(array) - 1
    result = -1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid:
            result = mid
            return result
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return result

result = find_fixedP(nums)
print(result)

