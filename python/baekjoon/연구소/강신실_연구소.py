'''
시작    11:19
끝      11:54
1. 벽을 세울 수 있는 모든 경우의 수를 구한다.
2. 바이러스를 퍼트린다.
3. 안전지대를 센다.
4. 최댓값을 구한다.
'''
import pdb
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
def get_virus_list(b):
    v_l = []
    for r, l in enumerate(b):
        for c, e in enumerate(l):
            if e == 2:
                v_l.append([r,c])
    return v_l
def get_all_loc(r,c):
    l = []
    for i in range(r):
        for j in range(c):
            l.append([i,j])
    return l
virus_l = get_virus_list(board)
point_l = get_all_loc(n,m)
ans = 0

def count_safe(b):
    cnt = 0
    for l in b:
        for e in l:
            # pdb.set_trace()
            if e == 0:
                cnt +=1
    return cnt
def spread_virus(candi):
    global board,n,m
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    n_board = [board[i][:] for i in range(len(board))]
    for r,c in candi:
        n_board[r][c]=1
    q = deque()
    for v in virus_l:
        q.append(v)
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<n and 0<=nc<m and n_board[nr][nc]==0:
                n_board[nr][nc]=2
                q.append([nr,nc])
    return n_board
def dfs(cnt, candi, idx):
    global ans, board
    if cnt == 3:
        safe = count_safe(spread_virus(candi))
        if safe>ans:
            ans = safe
    else:
        for i in range(idx, n*m):
            r, c = point_l[i]
            if board[r][c]==0:
                dfs(cnt+1, candi + [[r,c]], i+1)
dfs(0,[],0)
print(ans)