'''
시작    8:44
끛      10:10

1. 인접한 4개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장. (동시에) 
2. 기존 나무들은 인접한 4칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식한다.나눌때 생기는 나머지는 버린다.
3. 각 칸 중 제초제 뿌렸을 때 가장 나무 많이 박멸되는 칸에 뿌린다.
    제초제를 뿌릴 때 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
    c년만큼 제초제 남아있다가 c+1년만에 사라진다.
m년동안 총 박멸한 나무의 그루수?
'''
from asyncio import locks
import pdb
from collections import deque

n, m, k, C = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
herbicide_board = [[deque() for _ in range(n)] for _ in range(n)]
ans = 0
dr = [0,0,1,-1]
dc = [1,-1,0,0]

ddr = [1,1,-1,-1]
ddc = [1,-1,1,-1]

def grow():
    global n, board
    board_g = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if board[r][c]>0:
                cnt_trees = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0<=nr<n and 0<=nc<n and board[nr][nc]>0:
                        cnt_trees+=1
                board_g[r][c] =cnt_trees
    for r in range(n):
        for c in range(n):
            board[r][c] += board_g[r][c]
def reproduce():
    # 기존 나무들은 인접한 4칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식한다.나눌때 생기는 나머지는 버린다.
    global board, n, dr, dc, herbicide_board
    board_n = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if board[r][c]>0:
                new_tree_locs = []
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0<=nr<n and 0<=nc<n and board[nr][nc]==0 and True not in herbicide_board[nr][nc]:
                        new_tree_locs.append([nr,nc])
                if len(new_tree_locs)>0:
                    amt = board[r][c]//len(new_tree_locs)
                    for nr, nc in new_tree_locs:
                        board_n[nr][nc] += amt
    for r in range(n):
        for c in range(n):
            board[r][c] += board_n[r][c]

def weed():
    global board, n, ddr, ddc, herbicide_board, ans, C
    '''
    각 칸 중 제초제 뿌렸을 때 가장 나무 많이 박멸되는 칸에 뿌린다. => bfs
    제초제를 뿌릴 때 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
    c년만큼 제초제 남아있다가 c+1년만에 사라진다.
    <<버그>>나무를 없애는 것은 따로 생각해야한다.
    '''
    location = []
    maxx = -1e9
    for r in range(n):
        for c in range(n):
            if board[r][c]>=0:
                candi_n_trees = board[r][c]
                candi_l = [(r,c)]
                if board[r][c]>0:
                    q = deque()
                    q.append([r,c,0, 0])
                    q.append([r,c,1, 0])
                    q.append([r,c,2, 0])
                    q.append([r,c,3, 0])
                    while q:
                        cr, cc, d, t = q.popleft()
                        if t>=k:
                            continue
                        else:
                            nr = cr + ddr[d]
                            nc = cc + ddc[d]
                            if 0<=nr<n and 0<=nc<n:
                                candi_l.append((nr,nc))
                                if board[nr][nc]>0:
                                    q.append([nr,nc, d, t+1])
                                    candi_n_trees+=board[nr][nc]
                if maxx<candi_n_trees:
                    maxx = candi_n_trees
                    location = candi_l
                
    ans += maxx     
    for r in range(n):
        for c in range(n):
            if (r,c) in location:
                herbicide_board[r][c].append(True)
                if board[r][c]>0:
                    board[r][c]=0
            else:
                herbicide_board[r][c].append(False)
            if len(herbicide_board[r][c])>C:
                herbicide_board[r][c].popleft()



def solve():
    
    for _ in range(m):
        grow()
        reproduce()
        weed()
    print(ans)
solve()