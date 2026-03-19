n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1

for cur_coin in coins:
    if cur_coin > target:
        break

    target += cur_coin

print(target)