N, target = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)

result = binarySearch(array, target, 0, N-1)
if result == None:
    print("There's no the target in the array.")
else:
    print(result + 1)