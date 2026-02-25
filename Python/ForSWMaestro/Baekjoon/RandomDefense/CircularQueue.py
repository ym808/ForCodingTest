from collections import deque

n, m = map(int, input().split())
locs = list(map(int, input().split()))

q = deque()
for i in range(1, n + 1):
    q.append(i)

count = 0

for loc in locs:
    while q[0] != loc:
        if q.index(loc) > len(q) // 2:
            rightmost = q.pop()
            q.appendleft(rightmost)
            count += 1
        else:
            leftmost = q.popleft()
            q.append(leftmost)
            count += 1
    q.popleft()

print(count)
