'''
start   7:50
파이어스톰 단계 L을 결정 격자를 2^L크기 부분 격자로 나누고 모든 격자를 시계방향으로 90도 회전
이후 얼음 있는 칸 3개 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
(r,c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.
마법사 상어는 파이어스톰을 Q번 시전.
모든 파이어 스톰 시전 후 남아있는 얼음의 합, 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수는?
1. 부분 격자로 나눈다.
2. 각 부분을 회전시킨다.
3. 얼음이 3개 이상 인접하지 않은 칸을 녹인다.==> BFS코드 따로 짜기
4. 가장 큰 덩어리가 차지하는 칸의 개수를 구한다.
'''
from collections import deque, defaultdict

import pdb


N, Q = map(int, input().split())
N = 2**N
board = [list(map(int,input().split())) for _ in range(N)]
levels = list(map(int, input().split()))
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def print_board(b):
    for l in b:
        s = ""
        for e in l:
            s = s + str(e)+"\t"
        print(s)
def get_cnt_ice():
    global board, N
    cnt = 0
    for r in range(N):
        for c in range(N):
            cnt += board[r][c]
    return cnt
def get_max_size(b):
    global N
    maxx = 0
    d = defaultdict(int)
    for r in range(N):
        for c in range(N):
            d[b[r][c]]+=1
    for k, v in d.items():
        if k >0 and v>maxx:
            maxx = v
    return maxx
def get_block_board():
    global board, N, dr, dc
    block_board = [[0 for _ in range(N)] for _ in range(N)]
    v = [[False for _ in range(N)] for _ in range(N)]
    g_cnt = 0
    for r in range(N):
        for c in range(N):
            if v[r][c]==False and board[r][c]>0:
                g_cnt +=1
                q = deque()
                q.append([r,c])
                v[r][c]=True
                block_board[r][c]=g_cnt
                while q:
                    cr, cc = q.popleft()
                    for d in range(4):
                        nr = cr + dr[d]
                        nc = cc + dc[d]
                        if 0<=nr<N and 0<=nc<N and board[nr][nc]>0 and v[nr][nc]==False:
                            v[nr][nc]=True
                            q.append([nr,nc])
                            block_board[nr][nc]=g_cnt
        
        return block_board
def get_starting_points(lenn):
    global N
    l = []
    for r in range(0, N, lenn):
        for c in range(0, N, lenn):
            l.append([r,c])
    return l

def desolve_ice():
    global board, N, dr, dc
    melt_board = [[0 for _ in range(N)] for _ in range(N)]
    v = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c]<=0:
                continue
            cnt = 0
            for d in range(4):
                nr = r+dr[d]
                nc = c+dc[d]
                if 0<=nr<N and 0<=nc<N and board[nr][nc]>0:
                    cnt +=1
            if cnt<3:
                melt_board[r][c] +=1
    for r in range(N):
        for c in range(N):
            board[r][c] = max(0, board[r][c]-melt_board[r][c])


for level in levels:
    lenn = 2**level
    # 1. 시작점을 모두 구한다.
    starting_points = get_starting_points(2**level)
    # pdb.set_trace()
    n_board = [[0 for _ in range(N)] for _ in range(N)]
    # 2. 각 시작점에 대해 판을 돌린다.
    for sr, sc in starting_points:
        for r in range(lenn):
            for c in range(lenn):
                n_board[sr+c][sc+lenn-r-1] = board[sr+r][sc+c]
        
    board = n_board
    # 얼음을 녹인다.
    desolve_ice()
    
# 모든 얼음의 수를 구한다.
print(get_cnt_ice())
# 최대 얼음의 사이즈를 구한다 (BFS)
print(get_max_size(get_block_board()))



