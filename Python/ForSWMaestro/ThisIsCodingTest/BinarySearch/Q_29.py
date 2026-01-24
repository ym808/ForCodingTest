def is_install_possible(dist, count):
    last_router_loc = house_locs[0]
    count -= 1
    for house_loc in house_locs:
        if last_router_loc + dist <= house_loc:
            last_router_loc = house_loc
            count -= 1
    if count <= 0:
        return True
    else: return False
        


n, c = map(int, input().split())

house_locs = []

for _ in range(n):
    house_loc = int(input())
    house_locs.append(house_loc)
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