x, y, count = list(map(int, input().split()))
cab_locs = [list(map(int, input().split())) for _ in range(count)]

field = [[0] * x] * y

for loc in cab_locs:
    if field[loc[0], loc[1]] != 0: continue
    stack = []
    stack.append(loc)