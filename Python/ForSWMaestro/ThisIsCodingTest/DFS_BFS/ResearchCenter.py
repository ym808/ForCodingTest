from collections import deque
import copy
n, m = map(int, input().split())

researchCenter = []
for i in range(n):
    row = list(map(int, input().split()))
    researchCenter.append(row)

max_cleanAreas = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def printCenter(center):
    for i in range(n):
        for j in range(m):
            print(center[i][j], end=" ")
        print()
    print()

def bfs(Center, maxArea = False):
    copy_researchCenter = copy.deepcopy(Center)

    for x in range(n):
        for y in range(m):
            if copy_researchCenter[x][y] == 2:
                q = deque([(x, y)])
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        if copy_researchCenter[nx][ny] == 0:
                            copy_researchCenter[nx][ny] = 2
                            q.append((nx, ny))
    cleanAreas = 0
    for x in range(n):
        for y in range(m):
            if copy_researchCenter[x][y] == 0:
                cleanAreas += 1

    if maxArea == True:
        printCenter(copy_researchCenter)

    return cleanAreas

for i in range(n*m - 2):
    if researchCenter[i//m][i%m] == 1 or researchCenter[i//m][i%m] == 2: continue
    for j in range(i+1, n*m - 1):
        if researchCenter[j//m][j%m] == 1 or researchCenter[j//m][j%m] == 2: continue
        for k in range(j+1, n*m):
            if researchCenter[k//m][k%m] == 1 or researchCenter[k//m][k%m] == 2: continue
            researchCenter[i//m][i%m] = 1
            researchCenter[j//m][j%m] = 1
            researchCenter[k//m][k%m] = 1
            
            if max_cleanAreas < bfs(researchCenter):
                max_cleanAreas = bfs(researchCenter, True)
            
            researchCenter[i//m][i%m] = 0
            researchCenter[j//m][j%m] = 0
            researchCenter[k//m][k%m] = 0

print(max_cleanAreas)