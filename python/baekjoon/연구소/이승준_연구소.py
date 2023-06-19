# 시간: 10시25분~11시30분
import sys
sys.stdin = open('number9.txt','r')

# step1. 0이 있는 곳 중 3곳을 고르는 dfs실행
# step2. 3개의 좌표에 벽을 세웠다고 가정하고 bfs실행
# step3. dismap에 대해 0의 개수 count (dismap 3개의 최소값 계산)
# step4. 담아뒀다가 0의 갯수가 최대가 되는 값 return

# think1. 2의 갯수로 뭔가를 중간에서 cut하기에는 무리가 있어보인다
# think2. 완전탐색이 가장 효율적인 방법일까? (효율성을 올릴 수 있는 idea가 없을까?)

# idea1. 굳이 dismap3개를 구한 후 계산할 필요 없이 queue에 시작점(virus) 3개를 동시에 넣으면 되겠다!

from _collections import deque
N, M = map(int, input().split()) # row, col
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

virus_pos = []
path_pos = []
new_board = [[0] * M for _ in range(N)] # 벽(1)과 길(0)만 있는 board
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_pos.append([i,j])
        elif board[i][j] == 1:
            new_board[i][j] = -1
        elif board[i][j] == 0:
            path_pos.append([i,j])
virus_num = len(virus_pos)
path_num = len(path_pos)

import copy
def dismap(mat, answer):
    # new_mat = [[0] * M for _ in range(N)]
    new_mat = copy.deepcopy(mat)
    visited = [[False] * M for _ in range(N)]
    dx, dy = (1,0,-1,0), (0,1,0,-1)

    q = deque()
    for s in answer: # (중요) answer는 벽이다
        new_mat[s[0]][s[1]] = -1
    for s in virus_pos:
        q.append((s[0],s[1],0))
        visited[s[0]][s[1]] = True

    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False and new_mat[nx][ny] != -1: # (중요) mat대신 new_mat

                    visited[nx][ny] = True
                    q.append((nx,ny,dis+1))
                    new_mat[nx][ny] = dis+1

    for s in virus_pos:
        new_mat[s[0]][s[1]] = -1
    return new_mat


visited2 = [False] * path_num
result = []
def zero_count(mat):
    tmp = 0
    for i in range(N):
        tmp += mat[i].count(0)
    return tmp

max_val = 0
def dfs(cnt,answer,start):
    global max_val
    if cnt == 3:
        # if answer == [[0,1],[1,0],[3,5]]:
        #     print("ok", dismap(new_board, answer))
        #     max_tmp = max_val
        max_val = max(max_val, zero_count(dismap(new_board, answer)))
        # if max_tmp != max_val:
        #     print(dismap(new_board,answer), answer)
            # print(max_val, answer)
        return

    for i in range(start,path_num,1): # 이상~미만
        if visited2[i] == False and cnt <= 3:
            visited2[i] = True
            dfs(cnt+1,answer+[path_pos[i]],i)
            visited2[i] = False

dfs(0,[],0)
print(max_val)



