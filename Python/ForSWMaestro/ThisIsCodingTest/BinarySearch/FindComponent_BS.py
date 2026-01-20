import sys

N = int(input())
existing_list = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
requirement_list = list(map(int, sys.stdin.readline().rstrip().split()))

def binarySearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)

existing_list.sort()

for req in requirement_list:
    result = binarySearch(existing_list, req, 0, N-1)
    if result == None:
        print("no")
    else:
        print("yes")