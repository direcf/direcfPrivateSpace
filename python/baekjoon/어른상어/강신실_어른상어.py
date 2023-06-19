'''
시작 : 6:23
끝 : 

1. 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. spread_smell
2. 1초마다 모든 상어가 동시에 상하좌우칸 중 하나로 이동, 자신의 냄새를 그 칸에 뿌린다. move_shark
    냄새는 상어가 k번 이동하고 나면 사라진다.  

상어가 이동 방향을 결정할 때는 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
그런 칸이 없으면 자신의 냄새가 있는 칸으로 잡는다. (이 칸이 여러개 있으면 우선순위대로)
모든 상어가 이동한 후 한 칸에 여러 마리 남아있으면 가장 번호 작은 상어 제외하고 모두 격자 밖으로 쫓겨난다.
1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽

고민1. 격자 내 냄새는 어떻게 관리할 것인가?
1. 3중 배열로 관리 [상어번호, 몇초남았는지]
'''
import pdb
from collections import defaultdict

dr = [-1, 1, 0,0]
dc = [0,0,-1,1]

n, m, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
sharks = list(map(int,input().split()))
sharks_d = {}
smell_board = [[[0,0] for _ in range(n)] for _ in range(n)]
for i, shark in enumerate(sharks):
    sharks_d[i+1]=shark-1
for r in range(n):
    for c in range(n):
        if board[r][c]>0:
            kk = board[r][c]
            sharks_d[kk] = [r,c]+[sharks_d[kk]]

preference = {}
for i in range(m):
    l = []
    for _ in range(4):
        a, b, c, d = map(int,input().split())
        a -=1
        b -=1
        c -=1
        d -=1
        l.append([a,b,c,d])
    preference[i+1] = l

t = 0
flag = False

def spread_smell():
    global board, sharks_d, k, smell_board
    for sn, shark in sharks_d.items():
        sr, sc, sd = shark
        smell_board[sr][sc] = [sn, k]
def reduce_smell():
    global smell_board, n
    for r in range(n):
        for c in range(n):
            sn, left_time = smell_board[r][c]
            if sn>0:
                if left_time>1:
                    smell_board[r][c][1]-=1
                elif left_time==1:
                    smell_board[r][c] = [0,0]
def move_shark():
    '''
    상어가 이동 방향을 결정할 때는 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
    그런 칸이 없으면 자신의 냄새가 있는 칸으로 잡는다. (이 칸이 여러개 있으면 우선순위대로)
    모든 상어가 이동한 후 한 칸에 여러 마리 남아있으면 가장 번호 작은 상어 제외하고 모두 격자 밖으로 쫓겨난다.
    0, 1,2, 3는 각각 위, 아래, 왼쪽, 오른쪽
    '''
    global smell_board, preference, sharks_d, dr, dc, n
    for sn, shark in sharks_d.items():
        sr, sc, sd = shark
        
        preference_now = preference[sn][sd]
        # 먼저, 아무 냄새가 없는 칸이 있는지 확인해야한다.(순서대로)
        is_blank = False
        for d in preference_now:
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0<=nr<n and 0<=nc<n and smell_board[nr][nc][0]==0:
                is_blank = True
                sharks_d[sn] = [nr,nc,d]
                break
        # 아무 냄새가 없는 칸이 없으면, 본인 냄새가 있는 칸으로 간다.
        if is_blank == False:
            for d in preference_now:
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0<=nr<n and 0<=nc<n and smell_board[nr][nc][0]==sn:
                    sharks_d[sn] = [nr,nc,d]
                    break

def remove_shark():
    global sharks_d
    locations_cnt = defaultdict(list)
    for sn, shark in sharks_d.items():
        sr, sc, sd = shark
        locations_cnt[(sr, sc)].append(sn)
    for loc, shark_l in locations_cnt.items():
        if len(shark_l)>1:
            shark_l.sort()
            for i in range(1, len(shark_l)):
                del sharks_d[shark_l[i]]

def print_board(b):
    for l in b:
        s = ""
        for e in l:
            s = s + str(e)+"\t"
        print(s)

spread_smell()
while t<1000:
    t+=1
    move_shark()
    remove_shark()
    reduce_smell()
    spread_smell()
    
    
    if len(sharks_d.keys())==1:
        flag = True
        break

if flag == False:
    print(-1)
else:
    print(t)
