n = int(input())
fear_levels = sorted(list(map(int, input().split())))

groups = 0
person_count = 0
for fear_lev in fear_levels:
    person_count += 1
    if fear_lev <= person_count:
        groups += 1
        person_count = 0

print(groups)
