import sys 
input = sys.stdin.readline

s = input().rstrip()

nums = list("1234567890")

sum = 0
chars = []
c_count = 0

for c in s:
    if c in nums:
        sum += int(c)
        c_count += 1
    else:
        chars.append(c)

chars.sort()
for c in chars:
    print(c, end="")
if c_count != 0:
    print(sum)
