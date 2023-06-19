import sys
sys.stdin = open('number8.txt', 'r')


R,C,T = list(map(int, input().split()))
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

air_condition_pos = []
for i in range(R):
    if board[i][0] == -1:
        air_condition_pos.append([i,0]) # 위, 아래 순으로 들어간다
dx, dy = (1,0,-1,0), (0,-1,0,1)

rx1,ry1 = (0,-1,0,1), (1,0,-1,0)
rx2,ry2 = (0,1,0,-1), (1,0,-1,0)
# print(board)
def solve():
    for _ in range(T):

        # step1. diffusion
        board_tmp = [row[:] for row in board]
        for x in range(R):
            for y in range(C):
                if board_tmp[x][y] > 0: # 미세먼지 유무
                    cnt = 0
                    for dir in range(4):
                        nx, ny = x+dx[dir], y+dy[dir]
                        if 0<=nx<R and 0<=ny<C:
                            if [nx,ny] not in air_condition_pos:
                                board[nx][ny] += (board_tmp[x][y] // 5)
                                cnt += 1
                    board[x][y] -= (board_tmp[x][y] // 5) * cnt

        # step2. circulation
        # 회전이 일어나는데 -1은 움직이지 않는다
        board_tmp = [row[:] for row in board]  # 고정
        # 위쪽 반시계회전
        x, y = air_condition_pos[0]
        for dir in range(4):
            while True:
                nx, ny = x+rx1[dir], y+ry1[dir]
                if 0<=nx<R and 0<=ny<C:
                    if board_tmp[x][y] == -1: # 시작점
                        board[nx][ny] = 0
                        x, y = nx, ny
                        continue
                    elif board_tmp[nx][ny] == -1: # 끝점
                        break
                    else:
                        board[nx][ny] = board_tmp[x][y]
                        x, y = nx, ny
                else: # 범위에서 벗어나면 방향전환
                    break

        # 아래쪽 시계회전
        x, y = air_condition_pos[1]
        for dir in range(4):
            while True:
                nx, ny = x + rx2[dir], y + ry2[dir]
                if 0 <= nx < R and 0 <= ny < C:
                    if board_tmp[x][y] == -1:  # 시작점
                        board[nx][ny] = 0
                        x, y = nx, ny
                        continue
                    elif board_tmp[nx][ny] == -1:  # 끝점
                        break # 끝내기
                    else:
                        board[nx][ny] = board_tmp[x][y]
                        x, y = nx, ny
                else:  # 범위에서 벗어나면 방향전환
                    break
        print("2", board)
    total = 0
    for board_small in board:
        total += sum(board_small)
    return print(total+2) # 공기청정기인 -1,-1 을 상쇄하기 위해 2더하기

solve()
