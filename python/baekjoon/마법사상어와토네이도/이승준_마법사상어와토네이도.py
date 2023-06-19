# 시간: 10시23분~11시29분(1시간06분)
import sys
sys.stdin = open('number32.txt','r')

dx = ((1,1,1,2,-1,-1,-1,-2,0,0),(0,1,-1,0,0,1,-1,0,2,1),(1,1,1,2,-1,-1,-1,-2,0,0),(0,-1,1,0,0,-1,1,0,-2,-1))
dy = ((0,-1,1,0,0,-1,1,0,-2,-1),(1,1,1,2,-1,-1,-1,-2,0,0),(0,1,-1,0,0,1,-1,0,2,1),(1,1,1,2,-1,-1,-1,-2,0,0)) # 서 남 동 북
blow_percentage = (7,10,1,2,7,10,1,2,5,0)
dir_x, dir_y = (0,1,0,-1), (-1,0,1,0)
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def blowing(x,y,dir):
    global board
    total_sand = board[x][y]
    total_sand_tmp = total_sand
    for index, (plus_x, plus_y, percentage) in enumerate(zip(dx[dir], dy[dir], blow_percentage)):
        nx, ny = x+plus_x, y+plus_y
        if index == 9:  # 여기서는 나머지 알파를 계산
            if 0<=nx<N and 0<=ny<N:
                board[nx][ny] += total_sand_tmp
                board[x][y] = 0
            else:
                board[x][y] = 0
            continue

        if 0<=nx<N and 0<=ny<N: # (중요!!!!) index == 9랑 구분되어야 한다! 아니면 알파가 밖으로 나가지 못한
            tmp_sand = total_sand * percentage // 100
            total_sand_tmp -= tmp_sand
            board[nx][ny] += tmp_sand
        else: #### (중요!) 밖으로 나가는 경우에 대한 case도 생각해야 한다!
            tmp_sand = total_sand * percentage // 100
            total_sand_tmp -= tmp_sand

def solve():
    x, y = N//2, N//2
    cnt = 1
    dir = 0
    original_total_sand = 0
    for i in range(N):
        original_total_sand += sum(board[i])

    while True:
        for _ in range(cnt):
            x, y = x+dir_x[dir], y+dir_y[dir]
            blowing(x,y,dir)

        dir = (dir+1) % 4
        if x == 0 and y == -1:
            break

        for _ in range(cnt):
            x, y = x + dir_x[dir], y + dir_y[dir]
            blowing(x, y, dir)
        dir = (dir + 1) % 4
        cnt += 1

    last_total_sand = 0
    for i in range(N):
        last_total_sand += sum(board[i])
    print(original_total_sand - last_total_sand)
solve()

