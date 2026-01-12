# My Code
N = int(input())

hour, min, sec = 0,0,0
count = 0

while True:
    if hour % 10 == 3:
        count += 1
    elif min % 10 == 3 or min // 10 == 3:
        count += 1
    elif sec % 10 == 3 or sec // 10 == 3:
        count += 1

    if hour == N and min == 59 and sec == 59: break

    sec += 1
    if sec == 60:
        sec = 0
        min += 1
        if min == 60:
            min = 0
            hour += 1

print(count)

# Book Code

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)