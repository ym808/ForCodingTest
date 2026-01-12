space = int(input())
directions = input().split()

row = 1
col = 1

for direction in directions:
    match direction:
        case 'U':
            if row <= 1: continue
            row -= 1
        case 'D':
            if row > space: continue
            row += 1
        case 'R':
            if col > space: continue
            col += 1
        case 'L':
            if col <= 1: continue
            col -= 1
        case _:
            print("Invalid Direction")
print(row, col)
