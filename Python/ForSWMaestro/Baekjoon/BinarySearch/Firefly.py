n, cave_h = map(int, input().split())
heights = [int(input()) for _ in range(n)]

stalagmites = [height for height in heights[::2]]
stalactites = [height for height in heights[1::2]]

stalagmites.sort(reverse=True)
stalactites.sort(reverse=True)

min_targets = 10 ** 6
min_sectors = 0

for cur_cave_h in range(1, cave_h + 1):
    start = 0
    end = len(stalagmites) - 1
    last_target_idx = -1

    while start <= end:
        mid = (start + end) // 2

        if cur_cave_h - stalagmites[mid] <= 0:
            start = mid + 1
            last_target_idx = mid
        else:
            end = mid - 1

    target_stalagmites = last_target_idx + 1
    
    start = 0
    end = len(stalactites) - 1
    last_target_idx = -1

    while start <= end:
        mid = (start + end) // 2

        if cur_cave_h + stalactites[mid] > cave_h:
            start = mid + 1
            last_target_idx = mid
        else:
            end = mid - 1
    
    target_stalactites = last_target_idx + 1

    cur_targets = target_stalactites + target_stalagmites
    
    if cur_targets < min_targets:
        min_targets = cur_targets
        min_sectors = 1
    elif cur_targets == min_targets:
        min_sectors += 1

print(min_targets, min_sectors)
    