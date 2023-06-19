'''
1) 어떤 톱니바퀴를 어떻게 움직여야하는지 알아내기
    1. 시작부터 양옆으로 쭉 확인하기. (Q)
    오른쪽: 2-6
    왼쪽: 6-2
2) rotate 시키기
시작    10:25
끝      11:12
'''
import pdb
from collections import deque

gears = [str(input()) for _ in range(4)]
n_gears = [deque() for _ in range(4)]
for i, gear in enumerate(gears):
    for j in range(8):
        n_gears[i].append(int(gears[i][j]))
gears=n_gears
# print(gears)
# pdb.set_trace()
k = int(input())
def print_board(b):
    for l in b:
        s = ""
        for e in l:
            s = s+str(e) + "\t"
        print(s)
def get_score():
    global gears
    # print_board(gears)
    score = 0
    for i, gear in enumerate(gears):
        if gear[0]==1:
            score = score + (1<<i)
    return score
def get_moving_gears(n, d):
    global gears
    q = deque()
    moving_gears = []
    moving_gears.append([n,d])
    q.append([n,d,1])
    q.append([n,d,-1])
    while q:
        cn, cd, dir = q.popleft()
        nd = cd * -1
        # 오른쪽
        if dir == 1:
            nn = cn+1
            if nn<4 and gears[cn][2]+gears[nn][6]==1:
                q.append([nn, nd, 1])
                moving_gears.append([nn, nd])
        # 왼쪽
        if dir == -1:
            nn = cn-1
            if 0<=nn and gears[cn][6]+gears[nn][2]==1:
                q.append([nn, nd, -1])
                moving_gears.append([nn, nd])
    return moving_gears

def rotate(l):
    global gears
    for n, d in l:
        gears[n].rotate(d)
    

for _ in range(k):
    # print(k)
    n_gear, dir = map(int,input().split())
    n_gear -=1
    moving_gears = get_moving_gears(n_gear, dir)
    # print("print moving gears")
    # print(moving_gears)
    rotate(moving_gears)
print(get_score())