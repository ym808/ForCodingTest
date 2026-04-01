from collections import deque

def printMap():
    map = [[0] * n for _ in range(n)]
    for r, c in apple_locs:
        r -= 1
        c -= 1
        map[r][c] = 5
    for i in range(len(snake)):
        r, c = snake[i]
        if i == 0:
            map[r][c] = 2
        else:
            map[r][c] = 1
    
    for row in map:
        for col in row:
            print(f"{col:>2}", end="")
        print()
    print()

def change_direct(direct):
    global cur_direct 

    if direct == 'L':
        cur_direct -= 1
        if cur_direct == 0:
            cur_direct = 4
    elif direct == 'D':
        cur_direct += 1
        if cur_direct == 5:
            cur_direct = 1

n = int(input())
apple_num = int(input())
apple_locs = [tuple(map(int, input().split())) for _ in range(apple_num)]

l = int(input())
turns = deque()
for _ in range(l):
    t_time, direct = input().split()
    t_time = int(t_time)
    turns.append((t_time, direct))

time = 0
head = [0, 0]
cur_direct = 1
snake = deque([[0,0]])

while True:
    printMap()
    print(time)
    time += 1

    if cur_direct == 1:
        head[1] += 1
    elif cur_direct == 2:
        head[0] += 1
    elif cur_direct == 3:
        head[1] -= 1
    elif cur_direct == 4:
        head[0] -= 1
    
    crash = False
    
    # 경계를 넘어갔는가
    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n:
        print("Exceed line")
        break

    for body_coord in snake:
        
        if head[0] == body_coord[0] and head[1] == body_coord[1]:
            crash = True
            
    if crash == True:
        print("Crash")
        break
    
    # 사과를 먹었는가
    eat_apple = False
    for apple_loc in apple_locs:
        r, c = apple_loc[0] - 1, apple_loc[1] - 1
        if head[0] == r and head[1] == c:
            eat_apple = True
            apple_locs.remove(apple_loc)
            break

    if eat_apple == False:
        snake.pop()
    r, c = head
    snake.appendleft((r,c))

    if turns:
        turn_time, direct = turns[0]
        if time == turn_time:
            change_direct(direct)
            turns.popleft()
    
print(time)