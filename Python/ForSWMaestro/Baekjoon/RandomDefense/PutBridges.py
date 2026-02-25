import math

t = int(input())

cites = [list(map(int, input().split())) for _ in range(t)]

for lnr in cites:
    result = math.comb(lnr[1], lnr[0])
    print(result)
