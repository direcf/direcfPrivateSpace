'''
start:  7:34
end:    9:24
1. m명의 도망자는 2 종류로 나뉘는데, 좌우, 상하로 움직이는 도망자로 나뉜다.
    좌우는 항상 오른쪽부터 시작, 상하는 항상 아래쪽 부터 시작.
2. m명의 도망자가 먼저 동시에 움직이고, 다음으로 술래가 움직이는 순으로 움직인다. 총 k번 반복
3. 도망자가 움직일 때 현재 술래와의 거리가 3 이하인 도망자만 움직인다.(거리:  |x1 - x2| + |y1 - y2|)
    규칙
    1. 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
        움직이려는 칸에 술래가 있으면 움직이지 않는다.
        움직이려는 칸에 술래가 없으면 나무가 있어도 움직인다.
    2. 격자 벗어나는 경우
        방향을 반대로 튼다.
        바라보고 있는 방향으로 1칸 움직인다 했을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동
4. 술래는 달팽이 모양으로 움직인다. 
5. 이동 직후 바라보고 있는 방향 기준 현재 칸 포함 3칸 안에 있는 도망자를 잡는다. 하지만 나무가 있으면 못잡는다.
6. 술래가 도망자를 잡으면 다음 점수를 얻는다. t x 현재 턴에서 잡힌 도망자의 수

<<출력>>
k번에 걸쳐 술래잡기를 진행하는 동안 술래가 총 얻게된 점수

<<기능>>
도망자 움직이기
술래 움직이기 (BFS)
도망자 잡기
    잡을 도망자 구하기
    도망자 없애기
점수 더하기
도망자
'''
import pdb
from collections import defaultdict, deque
n,m,h,k = map(int,input().split())
runners = {}
watcher = [n//2, n//2,0,0,False]
dr_r = [[0,0],[1,-1]]
dc_r = [[1,-1],[0,0]]
dr_w = [-1,0,1,0]
dc_w = [0,1,0,-1]
lenn = 1
board = [[0 for _ in range(n)] for _ in range(n)]
is_tree = [[False for _ in range(n)] for _ in range(n)]
is_out = True
for i in range(1,m+1):
    r,c,type = map(int,input().split())
    type -=1
    runners[i]=[r-1,c-1,type,0]
for _ in range(h):
    r, c=map(int,input().split())
    is_tree[r-1][c-1]=True
board[watcher[0]][watcher[1]]=-1
def move_runners():
    '''
    도망자가 움직일 때 현재 술래와의 거리가 3 이하인 도망자만 움직인다.(거리:  |x1 - x2| + |y1 - y2|)
    규칙
    1. 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
        움직이려는 칸에 술래가 있으면 움직이지 않는다.
        움직이려는 칸에 술래가 없으면 나무가 있어도 움직인다.
    2. 격자 벗어나는 경우
        방향을 반대로 튼다.
        바라보고 있는 방향으로 1칸 움직인다 했을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동
    '''
    global runners, watcher, board, n
    wr, wc = watcher[:2]
    n_board = [[0 for _ in range(n)]for _ in range(n)]
    for i, runner in runners.items():
        r,c,type,d = runner
        distance = abs(r-wr)+abs(c-wc)
        if distance<=3:
            nr = r + dr_r[type][d]
            nc = c + dc_r[type][d]
            if 0<=nr<n and 0<=nc<n:
                if nr == wr and nc == wc:
                    # 움직이지 않는다.
                    continue
                else:   
                    runners[i] = [nr,nc,type,d]
            else:
                nd = (d+1)%2
                nr = r + dr_r[type][nd]
                nc = c + dc_r[type][nd]
                if nr == wr and nc == wc:
                    # 움직이지 않는다.
                    continue
                else:   
                    runners[i] = [nr,nc,type,nd]

def move_watcher():
    '''
    술래는 달팽이 모양으로 움직인다. 
    '''
    global n, board,  watcher, lenn, is_out
    q = deque()
    q.append(watcher)
    is_moved = False
    n_board = [[0 for _ in range(n)] for _ in range(n)]

    while q:
        cr, cc, cd, cnt, flag = q.popleft()
        if cnt == lenn:
            if flag:
                flag = False
                cnt = 0
                if is_out:
                    lenn = lenn+1
                    nd = (cd+1)%4
                else:
                    lenn = lenn-1
                    nd = (cd-1)%4
                watcher = [cr,cc,nd,cnt,flag]
                if is_moved==False:
                    q.append([cr,cc,nd,cnt,flag])
            else:
                flag = True
                cnt = 0
                if is_out:
                    nd = (cd+1)%4
                else:
                    nd = (cd-1)%4
                watcher = [cr,cc,nd,cnt,flag]
                if is_moved==False:
                    q.append([cr,cc,nd,cnt,flag])
        elif is_moved==False:
            nr = cr + dr_w[cd]
            nc = cc + dc_w[cd]
            n_board[nr][nc]=1
            nd = cd
            ncnt = cnt+1
            if cnt+1 == n-1 and nr == 0 and nc ==0 and is_out:
                is_out = False
                flag = True
                ncnt =1
                nd = (cd+2)%4
            if cnt+1 == 1 and nr == n//2 and nc == n//2 and is_out==False:
                is_out = True
                flag = False
                nd = (cd+2)%4
                ncnt=0
            watcher = [nr,nc,nd,ncnt,flag]
            is_moved = True
            q.append(watcher)
def print_board(b):
    for l in b:
        s = ""
        for e in l:
            s = s + str(e)+"\t"
        print(s)
def get_runners():
    global watcher, runners, is_tree, n
    l = []
    runner_board = [[[] for _ in range(n)] for _ in range(n)]
    for i, runner in runners.items():
        r,c,_,_ = runner
        runner_board[r][c].append(i)
    wr,wc,wd = watcher[:3]
    for i in range(3):
        nr = wr + dr_w[wd]*i
        nc = wc + dc_w[wd]*i
        if 0<=nr<n and 0<=nc<n and len(runner_board[nr][nc])>0 and is_tree[nr][nc]==False:
            l = l + runner_board[nr][nc]
    # print("runner board")
    # runner_board[wr][wc]=-1
    # print_board(runner_board)
    # print("watcher", watcher)
    return l
def remove_runners(l):
    global runners
    for i in l:
        del runners[i]
     

def solve():
    total_score = 0
    for i in range(1,k+1):
        move_runners()
        move_watcher()
        caught_runners = get_runners()
        remove_runners(caught_runners)
        
        total_score += len(caught_runners)*i
    print(total_score)
solve()

