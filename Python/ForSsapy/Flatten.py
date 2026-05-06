T = 10

for ts in range(1, T+1):
    dump = int(input())
    heights = list(map(int, input().split()))

    for _ in range(dump):
        max_h = max(heights)
        min_h = min(heights)

        if max_h - min_h == 0: break

        max_h_i = heights.index(max_h)
        min_h_i = heights.index(min_h)

        heights[max_h_i] -= 1
        heights[min_h_i] += 1

    print(f"#{ts} {max(heights) - min(heights)}")