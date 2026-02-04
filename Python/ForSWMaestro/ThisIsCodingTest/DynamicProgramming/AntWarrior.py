n = int(input())
storages = list(map(int, input().split()))

dp_table = [-1] * n

def return_foods(i):
    if i >= len(storages):
        return 0
    if dp_table[i] != -1:
        return dp_table[i]
    
    dp_table[i] = max(storages[i] + return_foods(i+2), return_foods(i+1))

    return dp_table[i]

print(return_foods(0))