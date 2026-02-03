def find_optim(i):
    match i:
        case 1 | 2 | 3 | 5: 
            return 1
    
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
    return min_result + 1

num = int(input())
print(find_optim(num))