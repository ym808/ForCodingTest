n = int(input())
storages = list(map(int, input().split()))

def return_foods(i):
    if i >= len(storages):
        return 0
    
    return storages[i] + max(return_foods(i+2), return_foods(i+3))

print(max(return_foods(0), return_foods(1)))