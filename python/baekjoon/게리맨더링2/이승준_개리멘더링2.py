# 시간: 19시15분~20시30분(1시간15분)
import sys
sys.stdin = open('number31.txt','r')

from collections import deque
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx, dy = (1,0,-1,0), (0,1,0,-1)

# def print_board(a):
#     for b in a:
#         s = ''
#         for c in b:
#             s = s + str(c) + ' '
#         print(s)
#     print()
# (핵심) 하늘색으로 색칠되어 있는 포지션들을 찾는 것이 가장 중요하다 기준점 x,y를 잡고 길이를 1씩 늘려가면서 나머지 3점의 존재 가능여부를 확인해야 한다
# step1. 기준점 x,y잡는 방식 생각하기 >>  x기준 0~n-3까지, y기준 1~n-2까지
# step2. 대각선 왼쪽, 오른쪽으로 확장하면서 3점의 좌표가 0<= <N내에 있는지 확인하기 (이걸 while문을 통해서 반복적으로 실행해야 한다)
def find_boarder(sx,sy):

    new_board = [] # sx,sy기준 가능한 모든 board 다 담을 예정
    # (중요!) max_d1, max_d2 찾기
    x, y = sx, sy

    # left결정
    d1 = 0
    while True:
        nx, ny = x+1+d1, y-1-d1
        if 0<=nx<N and 0<=ny<N:
            d1 += 1
        else:
            break

    # right결정
    d2 = 1
    while True:
        nx, ny = x+1+d2, y+1+d2
        if 0<=nx<N and 0<=ny<N:
            d2 += 1
        else:
            break

    # print(d1, d2) # 1 4
    # up = [x,y]
    # left = [x+i,y-i]
    # right = [x+j,y+j]
    # below = [x+i+j,y+j-i]
    for i in range(1,d1+1):
        for j in range(1,d2+1):
            if 0<=x+i+j<N and 0<=y+j-i<N: # below 결정
                mat = [[0] * N for _ in range(N)]
                mat[x][y] = 5
                # up -> left
                for r1 in range(1,i+1):
                    mat[x+r1][y-r1] = 5
                # up -> right
                for r2 in range(1,j+1):
                    mat[x+r2][y+r2] = 5
                # right -> below
                for r3 in range(1,i+1):
                    mat[x+j+r3][y+j-r3] = 5
                # left -> below
                for r4 in range(1,j+1):
                    mat[x+i+r4][y-i+r4] = 5

                # print_board(mat) # up, left, right, below 순으로 저장
                # four_points.append([[x,y],[x+i,y-i],[x+j,y+j],[x+i+j,x+j-i]])
                #################### <1,2,3,4 구역 색칠하기> >> 한꺼번에 구현 ###############
                visited = [[False] * N for _ in range(N)]
                q = deque()
                q.append((0,0))
                mat[0][0] = 1
                visited[0][0] = True
                while q:
                    xx, yy = q.popleft()
                    for k in range(4):
                        nx, ny = xx+dx[k], yy+dy[k]

                        if 0<=nx<x+i and 0<=ny<y+1:
                            if mat[nx][ny] != 5 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                mat[nx][ny] = 1


                q = deque()
                q.append((0,N-1))
                mat[0][N-1] = 2
                visited[0][N-1] = True
                while q:
                    # print_board(mat)
                    xx, yy = q.popleft()
                    for k in range(4):
                        nx, ny = xx+dx[k], yy+dy[k]

                        if 0<=nx<x+j+1 and y+1<=ny<N:
                            if mat[nx][ny] != 5 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                mat[nx][ny] = 2

                q = deque()
                q.append((N-1,0))
                mat[N-1][0] = 3
                visited[N - 1][0] = True
                while q:
                    xx, yy = q.popleft()
                    for k in range(4):
                        nx, ny = xx+dx[k], yy+dy[k]

                        if x+i<=nx<N and 0<=ny<y+j-i:
                            if mat[nx][ny] != 5 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                mat[nx][ny] = 3

                q = deque()
                q.append((N-1,N-1))
                mat[N-1][N-1] = 4
                visited[N - 1][N - 1] = True
                while q:
                    xx, yy = q.popleft()
                    for k in range(4):
                        nx, ny = xx+dx[k], yy+dy[k]

                        if x+j+1<=nx<N and y+j-i<=ny<N:
                            if mat[nx][ny] != 5 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                mat[nx][ny] = 4


                for xxx in range(N):
                    for yyy in range(N):
                        if mat[xxx][yyy] == 0:
                            mat[xxx][yyy] = 5
                # print_board(mat)
                # exit(0)
                new_board.append(mat)

    return new_board

#### (중요!) 이렇게 구하는 것의 단점: board_zip을 받아오는 과정이 너무 많은데 반복된다
# def divide_areas(board_zip, points_zip):
#     # 1번 구역색칠하기
#     q = deque()
#     q.append((0,0))
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x+dx[k], y+dy[k]
#
#             if 0<=nx<points_zip[1][] and 0<=ny<N:



def solve():
    min_val = int(1e9)
    # up을 여기서 결정!
    for x in range(0,N-2):
        for y in range(1,N-1):
            board_zip = find_boarder(x,y)

            # (중요!) 바로 score 계산... 근데 for문이 아무리 생각해도 너무 많다...
            for board5 in board_zip:
                score = [0] * 5
                for i in range(N):
                    for j in range(N):
                        if board5[i][j] == 1:
                            score[0] += board[i][j]
                        elif board5[i][j] == 2:
                            score[1] += board[i][j]
                        elif board5[i][j] == 3:
                            score[2] += board[i][j]
                        elif board5[i][j] == 4:
                            score[3] += board[i][j]
                        elif board5[i][j] == 5:
                            score[4] += board[i][j]
                min_val = min(min_val, abs(max(score) - min(score)))
    print(min_val)

solve()