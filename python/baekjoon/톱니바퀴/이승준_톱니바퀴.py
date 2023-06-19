# 시간: 11시30분~12시25분
import sys
sys.stdin = open('number10.txt','r')

from collections import deque
wheel = []
for _ in range(4):
    wheel.append(deque(map(int, input())))
N = int(input())
execute = []
for _ in range(N):
    execute.append(list(map(int,input().split()))) # (주의) 톱니바퀴번호와 관련해서 -1필요하다!!!



def dfs(start, rotation): # start는 이미 회전 확정
    if visited[start] == False:
        visited[start] = True
        rot_ox[start] = rotation

    # 내 옆자리 확인
    if 0<=start+1<4 and visited[start+1] == False:
        if wheel[start][2] == wheel[start+1][6]:
            pass
        else:
            dfs(start+1, rotation*-1)
            pass

    if 0<=start-1<4 and visited[start-1] == False:
        if wheel[start-1][2] == wheel[start][6]:
            pass
        else:
            dfs(start-1, rotation*-1)
            pass

def rotate(rot_ox):
    global wheel
    for index, rot in enumerate(rot_ox):
        wheel[index].rotate(rot)
    return

# (중요) 한번에 체크 가능하도록 만들기
def solve():
    global rot_ox,visited
    for ex in execute: # [[1, 1], [2, 1], [3, 1]]
        visited = [False] * 4 # (중요) 이거 초기화때문에 틀림
        rot_ox = [0,0,0,0]
        dfs(ex[0]-1, ex[1])
        rotate(rot_ox)
solve()

score = 0
for index, wh in enumerate(wheel):
    if index == 0:
        score += wheel[index][0] * 1
    elif index == 1:
        score += wheel[index][0] * 2
    elif index == 2:
        score += wheel[index][0] * 4
    elif index == 3:
        score += wheel[index][0] * 8
print(score)





# def rot(wheel_info,rot_info):
#     if rot_info[0] == 1:
#         if wheel[rot_info[0]-1][2] == wheel[rot_info[0]][6]: # NN, SS
#             wheel[rot_info[0]-1].rotate(rot_info[1])
#         else: # NS, SN
#             wheel[rot_info[0]-1].rotate(rot_info[1])
#             if wheel[rot_info[0]][2] == wheel[rot_info[0]+1][6]: # 돌리기 전에 check필
#                 wheel[rot_info[0]].rotate(rot_info[1]*-1)
#             else:
#                 wheel[rot_info[0]].rotate(rot_info[1]*-1)
#                 if wheel[rot_info[0]+1][2] == wheel[rot_info[0]+2][6]:
#                     wheel[rot_info[0]+1].rotate(rot_info[1])
#                 else:
#                     wheel[rot_info[0]+1].rotate(rot_info[1])
#                     wheel[rot_info[0]+2].rotate(rot_info[1]*-1)