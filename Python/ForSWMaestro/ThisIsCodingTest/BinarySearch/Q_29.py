def is_install_possible(dist, count):
    last_router_loc = house_locs[0]

    for _ in range(count - 1):
        next_router_loc = -1
        start = house_locs.index(last_router_loc) + 1
        end = len(house_locs) - 1

        while start <= end:
            mid = (start + end) // 2

            if house_locs[mid] == last_router_loc + dist:
                next_router_loc = house_locs[mid]
                break
            elif house_locs[mid] > last_router_loc + dist:
                next_router_loc = house_locs[mid]
                end = mid - 1
            else:
                start = mid + 1
        if next_router_loc == -1:
            return False
        last_router_loc = next_router_loc
    return True
        


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