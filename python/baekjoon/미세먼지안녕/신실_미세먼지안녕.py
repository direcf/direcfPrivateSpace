'''
미세먼지안녕
시작: 10:15
끝: 11:00
1. 미세먼지가 확산된다. defuse_dust
- 인접 4방향으로 확산
    1)공기청정기가 있거나, 2)칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 a_(r,c)//5
    확산시키고, 해당 칸에는 미세먼지가 그만큼 줄어든다.

3중 포문을 2중포문 , 1포문으로 나눠서 하면 시간복잡도를 낮출 수 있다.

2. 공기청정기 작동. fresh_air
    위쪽은 반시계, 아래쪽은 시계방향으로 순환
    한칸씩 모두 이동 => 새 보드에 다 채워넣기
'''
from collections import deque
import pdb
R,C,T = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(R)]
def get_loc():
    global board
    loc = []
    for r in range(R):
        if board[r][0]==-1:
            loc.append((r,0))
    return loc
location_airconditioner = get_loc()
dr = [0,0,1,-1] # 우 좌 하 상 
dc = [1,-1,0,0]


def print_board(b):
    for r in b:
        s = ""
        for e in r:
            s = s + "\t"+str(e)
        print(s)

def count_all_dust():
    global board
    sum = 0
    for rl in board:
        for e in rl:
            if e>0:
                sum+=e
    return sum

def defuse_dust():
    # 모든 위치에 대해서 확산이 가능한지 확인하고, 확산량을 계산한다.
    # 확산이 끝나고 현재 먼지량과 확산 먼지량을 더한다.
    global board, location_airconditioner, dr, dc

    d_board = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if (r,c) not in location_airconditioner:
                amt_dust = board[r][c]
                dif_amt = board[r][c]//5
                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    if 0<=nr<R and 0<=nc<C and ((nr,nc)  not in location_airconditioner):
                        d_board[nr][nc] += dif_amt
                        d_board[r][c]-= dif_amt
    for r in range(R):
        for c in range(C):
            board[r][c] += d_board[r][c]

def fresh_air():
    # 윗 부분은 반시계방향으로 공기를 순환시킨다.
    # 아랫 부분은 시계방향으로 공기를 순환시킨다.
    global R, C, board, dr, dc # 0 1 2 3 : 우 좌 하 상 
    clock_wise_direction = [0, 2, 1, 3]
    counter_clock_wise_direction = [0, 3, 1, 2]
    n_board = [[0 for _ in range(C)] for _ in range(R)]
    upper_r_idx = location_airconditioner[0][0]
    lower_r_idx = location_airconditioner[1][0]

    q = deque()
    q.append([upper_r_idx, 1, 0, board[upper_r_idx][1]])
    board[upper_r_idx][1]=0
    while q:
        cr, cc, cd, c_amt = q.popleft()
        if (cr,cc) in location_airconditioner:
            break
        
        while True:
            nr = cr + dr[counter_clock_wise_direction[cd]]
            nc = cc + dc[counter_clock_wise_direction[cd]]
            if 0 <= nr < R and 0 <= nc < C:
                if (nr,nc) not in location_airconditioner:
                    n_amt = board[nr][nc]
                    board[nr][nc] = c_amt
                    q.append([nr, nc, cd, n_amt])
                break
            else:
                cd = (cd+1)%4

    q = deque()
    q.append([lower_r_idx, 1, 0, board[lower_r_idx][1]])
    board[lower_r_idx][1]=0
    while q:
        cr, cc, cd, c_amt = q.popleft()
        if (cr,cc) in location_airconditioner:
            break
        
        while True:
            nr = cr + dr[clock_wise_direction[cd]]
            nc = cc + dc[clock_wise_direction[cd]]
            if 0 <= nr < R and 0 <= nc < C:
                if (nr,nc) not in location_airconditioner:
                    n_amt = board[nr][nc]
                    board[nr][nc] = c_amt
                    q.append([nr, nc, cd, n_amt])
                break
            else:
                cd = (cd+1)%4


for _ in range(T):
    defuse_dust()
    fresh_air()
print(count_all_dust())