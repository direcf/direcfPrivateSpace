N, M, K, C = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx, dy = (1,0,-1,0), (0,1,0,-1)
dx2,dy2 = (1,-1,1,-1),(1,1,-1,-1)

from collections import deque
result = 0

def grow():
    global board # UnboundLocalError: local variable 'board' referenced before assignment
    for i in range(N):
        for j in range(N):
            # if board[i][j] != -1 and board[i][j] != 0:
            if board[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]

                    if 0<=nx<N and 0<=ny<N:
                        # if board[nx][ny] != -1 and board[nx][ny] != 0:
                        if board[nx][ny] > 0:
                            cnt += 1
                board[i][j] += cnt
import copy
def reproduce():
    global board
    new_board = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            # if new_board[i][j] != -1 and new_board[i][j] != 0:
            if new_board[i][j] > 0:
                q = deque()
                cnt = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]

                    if 0<=nx<N and 0<=ny<N:
                        if new_board[nx][ny] == 0:
                            cnt += 1
                            q.append((nx,ny))

                for pos in q:
                    board[pos[0]][pos[1]] += new_board[i][j] // cnt


def killing():
    global result # (중요) 이건 왜 해야하지??
    pos = []
    value = []
    for i in range(N):
        for j in range(N):
            # if board[i][j] != -1 and board[i][j] != 0:
            if board[i][j] > 0:
                total = board[i][j]
                pos.append([[i,j]])
                for r in range(4):
                    for k in range(K): # 0,1,2 퍼져나가는 횟수
                        nx, ny = i+dx2[r]*(k+1), j+dy2[r]*(k+1)

                        if 0<=nx<N and 0<=ny<N:
                            if board[nx][ny] > 0:
                                pos[-1].append([nx,ny])
                                total += board[nx][ny]
                            elif board[nx][ny] == 0:
                                pos[-1].append([nx,ny])
                            elif board[nx][ny] == -1: # (중요!) -1을 만나면 그곳은 넘어가지 않게 해야 한다
                                break
                value.append(total)
    for po in pos[value.index(max(value))]: # (2, 3) # C = 1인 경우,
        if board[po[0]][po[1]] > 0:
            result += board[po[0]][po[1]]
        board[po[0]][po[1]] = -2-C

def clearing():
    global board
    for i in range(N):
        for j in range(N):
            if board[i][j] == -2:
                board[i][j] = 0
            elif board[i][j] < -2:
                board[i][j] += 1

def solve():
    for _ in range(M):
        grow()
        reproduce()
        killing()
        clearing()
    print(result)



solve()