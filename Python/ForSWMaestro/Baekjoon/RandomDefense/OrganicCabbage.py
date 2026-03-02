height, width, count = list(map(int, input().split()))
cab_locs = [tuple(map(int, input().split())) for _ in range(count)]

field = [[0] * width for _ in range(height)]

for loc in cab_locs:
    row, col = loc[0], loc[1]
    field[row][col] = 1
    
q = []
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

while cab_locs:
    q.append(cab_locs.pop())

    while q:
        cab_loc = q.pop()
        cur_r, cur_c = cab_loc[0], cab_loc[1]

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if next_r < 0 or next_r >= height or next_c < 0 or next_c >= width: continue
            if field[next_r][next_c] == 0: continue

            