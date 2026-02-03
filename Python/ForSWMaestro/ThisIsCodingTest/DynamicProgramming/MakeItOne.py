num = int(input())
table = [0] * 30001

table[1] = 0
table[2] = 1
table[3] = 1
table[4] = 2
table[5] = 1

for i in range(6, 30001):
    prev_results = []
    if i % 5 == 0:
        prev_result = table[i // 5]
        prev_results.append(prev_result)
    if i % 3 == 0:
        prev_result = table[i // 3]
        prev_results.append(prev_result)
    if i % 2 == 0:
        prev_result = table[i // 2]
        prev_results.append(prev_result)
        
    prev_result = table[i - 1]
    prev_results.append(prev_result)

    min_result = min(prev_results)
    table[i] = min_result + 1

print(table[num])