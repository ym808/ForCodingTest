def is_install_possible(dist, count):
    last_router_loc = house_locs[0]
    installed = 1
    for i in range(1, n):
        if last_router_loc + dist <= house_locs[i]:
            last_router_loc = house_locs[i]
            installed += 1
            if installed >= count:
                return True
    return False
        
n, c = map(int, input().split())

house_locs = [int(input()) for _ in range(n)]
house_locs.sort()

start = 1
end = house_locs[-1] - house_locs[0]
max_dist = 0

while start <= end:
    mid = (start + end) // 2

    if is_install_possible(mid, c):
        start = mid + 1
        max_dist = mid
    else:
        end = mid - 1
print(max_dist)