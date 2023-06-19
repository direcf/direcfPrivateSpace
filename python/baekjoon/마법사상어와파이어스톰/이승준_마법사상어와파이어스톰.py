import sys
sys.stdin = open('number30.txt','r')
# 시간: 18시14분~18시45분(31분)

def print_board(a):
    for b in a:
        s = ''
        for c in b:
            s = s + str(c) + ' '
        print(s)
    print()


# step1. rotation module >> 기준점(step이용)을 잡아주는 것이 추가되어야 한다
# step2. melting module >> 인접한 얼음이 2이하인 점을 모두 파악하기 + (-1) 하기
# step1, step2 반복

# step3. 가장 큰 얼음 덩어리 찾기 (맨 마지막에)
# step4. summation_calc module
from collections import deque
N, Q = map(int, input().split())
board = []
for _ in range(2**N):
    board.append(list(map(int, input().split())))
if Q == 1:
    M = [int(input())]
else:
    M = list(map(int, input().split()))
dx, dy = (1,0,-1,0), (0,1,0,-1)

def summation_calc(mat):
    summation = 0
    for i in range(2**N):
        summation += sum(mat[i])
    return summation

def rotation(mat, L):
    # print_board(mat)
    if L == 0:
        return mat
    step = 2**L # L=1 >> step=2
    length = len(mat)
    new_board = [[0] * length for _ in range(length)]
    for sx in range(0,length,step):
        for sy in range(0,length,step):
            for i in range(step):
                for j in range(step):
                    new_board[sx+j][sy+step-1-i] = mat[sx+i][sy+j] # (중요!) 90도 회전 >> 여기선 list(zip(*mat))방법을 쓸 수가 없다 (부분 회전이 실천되어야 하므로)
    # print()
    # print_board(new_board)
    return new_board

def melting(mat):
    length = len(mat)
    minus_pos = []
    for x in range(length):
        for y in range(length):
            if mat[x][y] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]

                    if 0<=nx<length and 0<=ny<length:
                        if mat[nx][ny] > 0:
                            cnt += 1

                if cnt <= 2:
                    minus_pos.append([x,y])
    # print(minus_pos) # [[0, 0], [0, 7], [7, 0], [7, 7]]
    print("minus_pos", minus_pos)
    for pos in minus_pos:
        mat[pos[0]][pos[1]] -= 1

    return mat

def max_sizing(mat):
    length = len(mat)
    visited = [[False] * length for _ in range(length)]
    max_size = 0
    for i in range(length):
        for j in range(length):
            if visited[i][j] == False and mat[i][j] > 0:
                visited[i][j] = True
                q = deque()
                q.append((i,j))
                cnt = 1

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]

                        if 0<=nx<length and 0<=ny<length:
                            if visited[nx][ny] == False and mat[nx][ny] > 0:
                                cnt += 1
                                q.append((nx,ny))
                                visited[nx][ny] = True

                max_size = max(max_size,cnt)
    return max_size

# (의문) melting과 max_sizing은 따로 해야할까? >> 그렇다. melting은 여러번 돌아가지만 max_sizing은 마지막에만 필요하기 때문!
def solve():
    global board

    for m in M:
        # print("STEP")
        # print(summation_calc(board))
        # print_board(board)

        board = rotation(board, m)
        # print("rot after")
        # print_board(board)
        board = melting(board)


    # print_board(board)
    print(summation_calc(board))
    print(max_sizing(board))

solve()