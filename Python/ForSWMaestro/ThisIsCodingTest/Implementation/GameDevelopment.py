row_size, col_size = map(int, input().split())
row, col, direction = map(int, input().split())
next_row, next_col = row, col
matrix = []
visited_places = [(row, col)]
count = 0
visited = 0
moved = 0

for _ in range(row_size):
    cols = list(map(int, input().split()))
    matrix.append(cols)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    for _ in range(4):
        direction -= 1
        if direction == -1 : direction = 3
        impossible = 0
        moved = 0        

        next_row = row + dx[direction]
        next_col = col + dy[direction]

        if matrix[next_row][next_col] == 1: 
            impossible = 1
        else:
            for (visited_row, visited_col) in visited_places:
                if visited_row == next_row and visited_col == next_col:
                    impossible = 1
                    break
        if impossible: 
            next_row = row
            next_col = col
            continue
        moved = 1
        break

    if moved == 1:
        visited_places.append((next_row, next_col))
    else:
        next_row = row - dx[direction]
        next_col = col - dy[direction]
        if matrix[next_row][next_col] == 1: break
    row = next_row
    col = next_col
    count += 1
print(count)