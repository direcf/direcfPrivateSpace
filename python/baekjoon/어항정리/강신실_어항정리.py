'''
어항정리
1.물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다. 
    만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 1마리씩 넣는다. 
2. 1칸씩 회전시켜서 쌓는다.
3. 물고기옮기기 작업을 한다.
4. 1열로 펴는 작업을 한다.
5. 반으로 접는 작업을 2회 시행한다.
6. 물고기 옮기기 작업을 한다.
7. 1열로 펴는 작업을 한다.

어항의 수 N, 각 어항에 들어있는 물고기의 수가 주어진다. 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 정리해야하는지 구해보자.

'''

from collections import deque, defaultdict
import enum
import pdb
import queue
from tkinter import E
n, k = map(int,input().split())
fishes_ = list(map(int,input().split()))
fishes_r = deque()
fishes_c = deque()
rq = deque()
for fish in fishes_:
    q = deque()
    q.append(fish)
    fishes_c.append(q)
    rq.append(fish)
fishes_r.append(rq)
def print_board(b):
    for l in b:
        print(l)

def rotate_tanks(l):
    global fishes_r, fishes_c
    square = list(fishes_c)[:l]
    print(square)
    h = len(square[0])
    new_square = deque()
    for i in range(l-1,-1,-1):
        print("hereeee", i)
        q = deque()
        for j in range(h):
            print("hhhh",j)
            q.append(square[i][j])
        new_square.append(q)
    return new_square



def c_to_r(b):
    
    R = len(b[0])
    C = len(b)
    n_fishes_r = deque()
    for _ in range(R):
        n_fishes_r.append(deque())
    for c, q in enumerate(b):
        for r, e in enumerate(q):
            n_fishes_r[r].append(e)
    print(b)
    for i in range(C):
        print(b[i])
    print("C TO R")
    for i in range(R):
        print(n_fishes_r[i])
    return n_fishes_r

def r_to_c(b):
    R = len(b)
    C = len(list(b[0]))
    for i in range(R):
        print(b[i])
    n_fishes_c = deque()
    for _ in range(C):
        n_fishes_c.append(deque())
    for r, q in enumerate(b):
        for c, e in enumerate(list(q)):
            # n_board[r][c]=e
            print(len(n_fishes_c), c)
            n_fishes_c[c].append(e)
    print("R tO C")
    for i in range(C):
        print(n_fishes_c[i])
    return n_fishes_c       




def stack(a, b):
    global fishes_r, fishes_c
    b_r = c_to_r(b)
    for q in a:
        b_r.append(q)
    fishes_r = b_r
    fishes_c = r_to_c(fishes_r)
    

def rotate_and_stack_tank():
    global fishes_r, fishes_c
    length = 1
    while True:
        print(fishes_c)

        rotated_tanks = rotate_tanks(length)
        length = len(rotated_tanks[0])
        if length*2>len(fishes_c):
            break
        stack(rotated_tanks, list(fishes_c)[len(rotated_tanks):])
        print("??")
        print(rotated_tanks)
            
def add_fish(locs):
    global fishes_c, fishes_r
    for r, c in locs:
        fishes_c[c][r] +=1
        fishes_r[r][c] +=1

def get_max():
    global fishes_c
    maxx = 0
    l = []
    for c, q in enumerate(list(fishes_c)):
        for r, e in enumerate(list(q)):
            if e>maxx:
                l = [[r,c]]
                maxx = e
            elif e == maxx:
                l.append([r,c])
    return maxx, l
def get_min():
    global fishes_c
    minn = 1e9
    l = []
    for c, q in enumerate(list(fishes_c)):
        for r, e in enumerate(list(q)):
            if e<minn:
                l = [[r,c]]
                minn = e
            elif e == minn:
                l.append([r,c])
    return minn, l
def sqeeze():
    global fishes_c, fishes_r
    n_fishes_c = deque()
    n_fishes_r = deque()
    n_l = []

    for c, q in enumerate(fishes_c):
        for r, e in enumerate(q):
            n_l.append(e)
    q_l = deque()
    for e in n_l:
        q = deque()
        q.append(e)
        n_fishes_c.append(q)
        q_l.append(e)
    n_fishes_r.append(q_l)
    fishes_c = n_fishes_c
    fishes_r = n_fishes_r
def move_fish():
    global fishes_c, fishes_r
    R= len(fishes_r)
    C = len(fishes_c)
    d_board = [[0 for _ in range(C)] for _ in range(R)]
    board = [[-1 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(len(fishes_r[r])):
            print(r, c, board, fishes_r[r])
            board[r][c] = fishes_r[r][c]
    for r in range(R):
        for c in range(C):
            if board[r][c]>-1:
                for d in range(2):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0<=nr<R and 0<=nc<C and board[nr][nc]>-1:
                        d_fish = abs(board[r][c]-board[nr][nc])//5
                        if d_fish>0:
                            if max(board[r][c], board[nr][nc])==board[r][c]:
                                d_board[r][c] -= d_fish
                                d_board[nr][nc] += d_fish
                            else:
                                d_board[r][c] += d_fish
                                d_board[nr][nc] -= d_fish

    for l in d_board:
        print(l)
    pdb.set_trace()
    tmp = deque()
    for r in range(R):
        for c in range(C):
            board[r][c] += d_board[r][c]
    for r in range(R):
        q = deque()
        for c in range(C):
            if board[r][c]>-1:
                q.append(board[r][c])
        tmp.append(q)
    fishes_r = tmp
    fishes_c = r_to_c(fishes_r)
    print(fishes_r)
    pdb.set_trace()
def fold_and_stack_tank():
    global fishes_r, fishes_c
    rotated_tanks = rotate_tanks(len(fishes_c)//2)


dr = [1,0]
dc = [0,1]
def solve():
    dif = 0
    maxx, max_l = get_max()
    minn, min_l = get_min()
    pdb.set_trace()
    dif = maxx-minn
    ans = 0
    while dif>k:
        ans+=1
        minn, min_l = get_min()
        add_fish(min_l)
        rotate_and_stack_tank()
        move_fish()
        sqeeze()
        print(fishes_c)
        print(fishes_r)
        fold_and_stack_tank()
        # move_fish()
        # sqeeze()
        # dif = get_max(fishes)-get_min(fishes)
    print(ans)
    
solve()
        
        
