num = int(input())
table = [0] * 30001

def find_optim(i):
    if i == 1:
        return 0
    
    if table[i] != 0:
        return table[i]

    prev_results = []
    if i % 5 == 0:
        prev_result = find_optim(i // 5)
        prev_results.append(prev_result)
    if i % 3 == 0:
        prev_result = find_optim(i // 3)
        prev_results.append(prev_result)
    if i % 2 == 0:
        prev_result = find_optim(i // 2)
        prev_results.append(prev_result)
        
    prev_result = find_optim(i - 1)
    prev_results.append(prev_result)

    min_result = min(prev_results)
    table[i] = min_result + 1
    return table[i]

print(find_optim(num))