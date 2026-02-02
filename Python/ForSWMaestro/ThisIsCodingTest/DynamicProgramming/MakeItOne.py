num = int(input())
table = [0] * 30001
count = 0

while num > 1:
    if table[num] == 0:
        if num % 5 == 0:
            num //= 5
        elif num % 3 == 0:
            num //= 3
        elif num % 2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1
    else:
        count += table[num]

print(count)