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

while True:
    for _ in range(4):
        direction -= 1
        impossible = 0
        moved = 0        

        match direction:
            case 0:
                next_row = row - 1
            case 1:
                next_col = col + 1
            case 2:
                next_row = row + 1
            case -1:
                next_col = col - 1
                direction = 3

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
        match direction:
            case 0:
                next_row = row + 1
            case 1:
                next_col = col - 1
            case 2:
                next_row = row - 1
            case 3:
                next_col = col + 1
        if matrix[next_row][next_col] == 1: break
    row = next_row
    col = next_col
    count += 1
print(count)