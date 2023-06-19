# 시간:10시25분~11시20분 (12시00분 틀림..) (12시10분 맞춤but시간초과...)
import sys
sys.stdin = open('number14.txt','r')
# (중요) CCTV의 회전이 조금 어렵다
# CCTV의 회전을 dfs로 구해야 하나?
# 1: 경우4개, 2: 경우2개, 3:경우4개, 4:경우4개, 5:경우1개
# 만약 cctv 1 3개, 2 2개가 존재하는 경우
# (1,dir1), (1,dir2), (1,dir3), (2,dir1), (2,dir2)의 경우를 모두 구해야한다

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cctv_pos = []
cctv = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6: # 벽과 길이 아닌경우
            cctv_pos.append([i,j])
            cctv.append(board[i][j])

# 방향을 rot으로 나타낼 수 있을 것 같다
# dx1,dy1 = (1,0,-1,0),(0,1,0,-1) # down,right,up,left
# dx2,dy2 = (0,-1,0,1),(1,0,-1,0)
# dx3,dy3 = (-1,0,1,0),(0,-1,0,1)
# dx4,dy4 = (0,1,0,-1),(-1,0,1,0)
# dx,dy = ((1,0,-1,0),(0,-1,0,1),(-1,0,1,0),(0,1,0,-1)),((0,1,0,-1),(1,0,-1,0),(0,-1,0,1),(-1,0,1,0))
dx,dy = (1,0,-1,0),(0,1,0,-1)
direction2 = [[[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]

# print("cctv pos :", cctv_pos) # [[1, 1], [3, 4], [5, 5]]
# print("cctv :", cctv) # [2, 2, 5]



# step1. 감시
from collections import deque
import copy
def surveillance(mat,cases):
    # 방향을 잡아야 한다 (4방향으로 진행)
    result = []
    # 기준점을 잡아야 한다
    for ca in cases: # 방향 시작방향 설정
        visited = [[False] * M for _ in range(N)]
        new_mat = copy.deepcopy(mat)

        for index, (pos, kind) in enumerate(zip(cctv_pos, cctv)): # 각각의 시작점이 다를 수 있다

            check_list = direction2[kind-1][ca[index]]
            # print(check_list)
            for j in check_list:
                dir_x, dir_y = dx[j], dy[j]
                q = deque()
                q.append(pos)
                visited[pos[0]][pos[1]] = True

                while q:
                    x,y = q.popleft()
                    nx, ny = x+dir_x, y+dir_y

                    if 0<=nx<N and 0<=ny<M:
                        if visited[nx][ny] == False and mat[nx][ny] == 0:
                            visited[nx][ny] = True
                            new_mat[nx][ny] = '#'
                            q.append((nx,ny))

                        elif visited[nx][ny] == False and mat[nx][ny] == 6:
                            # 다음 칸이 벽이면 이쪽 방향진행은 끝난것
                            break

                        # 감시카메라는 무시가능
                        elif mat[nx][ny] == 1 or mat[nx][ny] == 2 or mat[nx][ny] == 3 or mat[nx][ny] == 4 or mat[nx][ny] == 5:
                            q.append((nx,ny))

                        #### (중요!) 이것도 필요하다 (new_mat[nx][ny] == '#') mat이 아닌 new_mat이다!!!
                        elif visited[nx][ny] == True and new_mat[nx][ny] == '#':
                            q.append((nx,ny))

        # step2. 사각지대 count
        # print(new_mat)
        cnt = 0
        for i in range(N):
            for j in range(M):
                if new_mat[i][j] == 0:
                    cnt += 1
        result.append(cnt)
    print(min(result))

direction = [[0,1,2,3], [0,1], [0,1,2,3],[0,1,2,3],[0]]

# print("cctv :", cctv) # [2, 2, 5]
visited = [False]*len(cctv)
case = []
def dfs(cnt, answer):
    if cnt == len(cctv):
        case.append(answer)
        return

    for i in range(cnt,len(cctv),1): # 0,1,2
        if visited[i] == False:
            for new in direction[cctv[i]-1]:
                visited[i] = True
                dfs(cnt+1, answer+[new])
                visited[i] = False


dfs(0,[])
# 순서 맞는지 확인
# print(case)
# print(cctv)
surveillance(board,case)
