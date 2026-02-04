# top-down version(mine)
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

# bottom-up version(book)

dp_table = [-1] * n

dp_table[0] = storages[0]
dp_table[1] = max(storages[0], storages[1])

for i in range(2, n):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + storages[i])

print(dp_table[n-1])

# bottom-up no memory version(gpt)

dp_i_minus2 = storages[0]
dp_i_minus1 = max(storages[0], storages[1])

for i in range(2, n):
    dp_i = max(dp_i_minus1, dp_i_minus2 + storages[i])
    dp_i_minus2, dp_i_minus1 = dp_i_minus1, dp_i

print(dp_i)