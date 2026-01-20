N, target = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

result = binarySearch(array, target, 0, N-1)

if result == None:
    print("There's no the target in the array")
else:
    print(result + 1)