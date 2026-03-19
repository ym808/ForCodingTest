import sys
input = sys.stdin.readline

s = input().rstrip()

total = 0
has_num = False
chars = []

for c in s:
    if c.isdigit():
        total += int(c)
        has_num = True
    else:
        chars.append(c)

chars.sort()

result = "".join(chars)

if has_num:
    result += str(total)

print(result)