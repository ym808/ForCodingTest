import sys

n, req_length = map(int, input().split())
ddeok_lengths = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ddeok_lengths) - 1

while start <= end:
    
    mid = (start + end) // 2
    h = mid

    sum = 0
    for ddeok_len in ddeok_lengths:
        if ddeok_len > h:
            sum += ddeok_len - h
    
    if req_length == sum: break
    elif req_length > sum:
        end = mid - 1
    else:
        start = mid + 1
        result = h
        
print(result)