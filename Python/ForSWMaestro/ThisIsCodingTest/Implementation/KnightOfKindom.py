# My Code
positions = input()
col, row = positions[0], positions[1]
row = int(row)
col = ord(col)
count = 0
one = [1, -1]
two = [2, -2]
results = []

# E, W
for t in two:
    mcol = col + t
    for o in one:
        mrow = row + o
        results.append((mrow, mcol))

for t in two:
    mrow = row + t
    for o in one:
        mcol = col + o
        results.append((mrow, mcol))

for pair in results:
    if pair[0] < 9 and pair[0] > 0 and pair[1] < ord('i') and pair[1] > ord('a') - 1:
        count += 1
print(count)

# Book Code

input_data = input()
col = ord(input_data[0]) - ord('a') + 1
row = int(input_data[1])
count = 0

steps = [
    (-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)
]

for step in steps:
     next_row = row + step[0]
     next_col = col + step[1]

     if next_row < 9 and next_row > 0 and next_col < 9 and next_col > 0:
         count += 1
print(count)
