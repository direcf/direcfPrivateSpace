import sys
sys.stdin = open('number6.txt', 'r')
# 시간: 1시간 (11시20분~12시20분)
N, M = map(int, input().split())
x,y,dir = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx, dy = (-1,0,1,0), (0,1,0,-1) # 북,동,남,서
visited = [[False] * M for _ in range(N)]

def solve():
    global x,y,dir
    answer = 0
    while True:
        # print(answer)
        # 1. 현재 위치 청소 (x,y,dir)
        visited[x][y] = True
        answer += 1
        clean_up = 0
        rot_cnt = 0

        # 왼쪽 방향결정
        for _ in range(4):
            n_dir = (dir + 3) % 4 # 0(북) -> 3(서)
            nx, ny = x+dx[n_dir], y+dy[n_dir]

            # 2.1
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[nx][ny] == False:  # 움직이기 위해선 벽이 아님도 확인필요
                dir = n_dir # 방향바꾸기
                x,y = nx, ny # 위치 옮기기
                clean_up = 1
                break

            # 2.2
            else: # 다음방향으로 못 가면
                dir = n_dir
                rot_cnt += 1
                continue



        if clean_up == 1:
            continue

        if rot_cnt == 4:
            n_dir = (dir + 2) % 4 # 후진방향
            nx, ny = x + dx[n_dir], y + dy[n_dir]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0: # 후진가능
                x, y = nx, ny
                answer -= 1 # 후진은 카운트 안해야하기 때문에!!
                continue

            else: # 후진조차 불가능
                return print(answer)

solve()

