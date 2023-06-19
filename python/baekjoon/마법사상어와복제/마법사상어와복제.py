# 시간: 18시40분~20시30분(1시간50분)
import sys
sys.stdin = open('number11.txt','r')

# (check) 맨위왼쪽칸이 1,1로 나타내지므로 -1씩 해줘야한다 ()
# (check) 가장 많은 물고기를 먹는 방법이 여러개일 경우 sort필요? ()

from collections import deque
M,S = map(int, input().split())
q_fish_pos = deque()
q_fish_dir = deque()
q_shark_pos = deque()
q_fish_smell = deque()
for _ in range(M):
    tmp = list(map(int, input().split()))
    q_fish_pos.append([tmp[0]-1,tmp[1]-1])
    q_fish_dir.append(tmp[2]-1)

tmp = list(map(int, input().split()))
q_shark_pos.append([tmp[0]-1,tmp[1]-1])

# print(q_fish_pos, q_fish_dir, q_shark_pos) # deque([[3, 2], [0, 2], [1, 3], [1, 0], [2, 3]]) deque([5, 5, 2, 6, 4]) deque([[3, 1]])



# 설계가 중요한 문제라고 생각된다 (dict보다는 queue가 낫고, queue도 위치와 이동방향을 나누자) # [1,2] in q
# step1. 복사
# step2. 물고기 이동: 상어,물고기냄새,격자외부는 갈 수 없다 (현재방향이 이동불가라면 반시계45도 회전 -1)
# step3. 상어 이동: 3번이동 dfs (가장 많은 물고기를 잡아먹는 이동방법 선택, 그 방법이 여러개일 경우 사전순서대로 진행)
#        잡아먹힌 물고기는 물고기 냄새를 남긴다 # deque([],[],new)로 넣어주는 방식을 만들자
# step4. 2회전 연습에서의 냄새는 격자에서 사라진다 # 앞에 있는 친구 pop()
# step5. step1에서의 물고기 상태로 복제되어 나타난다 (이동중에 상어와 만나야 하므로 생기자마자 잡아먹히지는 않는다)

dx, dy = (0,-1,-1,-1,0,1,1,1),(-1,-1,0,1,1,1,0,-1)
ddx, ddy = (-1,0,1,0),(0,-1,0,1) # 상좌하우 (shark의 움직임)

def fish_copy():
    global q_fish_pos, q_fish_dir, q_fish_pos_tmp, q_fish_dir_tmp
    q_fish_pos_tmp = [i[:] for i in q_fish_pos]
    q_fish_dir_tmp = [i for i in q_fish_dir]
    # q_fish_pos_tmp = deque(q_fish_pos_tmp)
    # q_fish_dir_tmp = deque(q_fish_dir_tmp)


def fish_move():
    global q_fish_pos, q_fish_dir
    new_q_pos = deque()
    new_q_dir = deque()
    for fish_pos, fish_dir in zip(q_fish_pos, q_fish_dir):
        # print(fish_pos, fish_dir) # [3, 2] 4
        for i in range(8):
            # (중요) 반시계 fish_dir - i / 시계 fish_dir + i
            nx, ny = fish_pos[0]+dx[(fish_dir-i)%8],fish_pos[1]+dy[(fish_dir-i)%8]
            if 0<=nx<4 and 0<=ny<4:
                if [nx,ny] not in q_shark_pos:
                    if [nx,ny] not in q_fish_smell:
                        new_q_pos.append([nx,ny])
                        new_q_dir.append((fish_dir-i) % 8)
                        # print(nx, ny, (fish_dir-i) % 8)
                        break
    q_fish_pos, q_fish_dir = new_q_pos, new_q_dir
    # print(q_fish_pos, q_fish_dir)
    # print(new_q_pos, new_q_dir)

# 2개의 list를 만들어서 하나는 3번 이동 후, shark의 pos와 먹은 물고기의 pos
# shark가 3번이동 (상,상,하) 이런 방식으로 이동가능한 모든 경우 계산
# 각 이동마다 물고기를 먹은 경우,물고기 리스트에서 그 물고기를 backtracking과 같이 순간적으로 없애줘야 한다
# 이동횟수가 3이 되면, 먹은 물고기 리스트를 update시키자

shark_pos_result = []
fish_pos_result = []
fish_dir_result = []
dead_fish_cnt_result = 0
dead_fish_list_result = []

def dfs(cnt, shark_pos, fish_pos, dead_fish_cnt,dead_fish_list, fish_dir):
    global shark_pos_result, fish_pos_result, dead_fish_cnt_result, dead_fish_list_result, fish_dir_result
    if cnt == 3:
        # print(shark_pos, fish_pos,dead_fish_cnt, dead_fish_list)
        if dead_fish_cnt > dead_fish_cnt_result:
            dead_fish_cnt_result = dead_fish_cnt
            dead_fish_list_result = dead_fish_list
            shark_pos_result = shark_pos
            fish_pos_result = fish_pos
            fish_dir_result = fish_dir

        return
    # print(shark_pos, fish_pos) # deque([[3, 1]]) deque([[3, 3], [0, 3], [0, 2], [2, 1], [1, 3]])
    if len(shark_pos) == 0:
        return
    tmp = shark_pos.popleft()
    x, y = tmp[0], tmp[1]

    for i in range(4):
        nx, ny = x+ddx[i], y+ddy[i]
        if 0<=nx<4 and 0<=ny<4: # 격자내부, fish
            # 물고기 리스트에 nx,ny가 있는지 확인
            if [nx,ny] in fish_pos: # (중요) 이러면 방향성은 어떻게 없애지? vs not in을 쓰려면 pos와 방향을 나누는게 좋은데...
                dfs(cnt+1,deque([[nx,ny]]),deque([i for i in fish_pos if i not in [[nx,ny]]]), dead_fish_cnt+fish_pos.count([nx,ny]), dead_fish_list+[[nx,ny]], deque([fish_dir[index] for index, i in enumerate(fish_pos) if i not in [[nx,ny]]]))
            else:
                dfs(cnt+1,deque([[nx,ny]]),fish_pos,dead_fish_cnt,dead_fish_list, fish_dir)


def shark_move():
    dfs(0,q_shark_pos, q_fish_pos, 0,[],q_fish_dir)


def smelling(): # 2회연속일 경우
    global q_fish_smell, dead_fish_list_result
    q_fish_smell.append(dead_fish_list_result)
    dead_fish_list_result = []

def posing():
    global shark_pos_result, fish_pos_result, q_fish_pos, q_shark_pos, fish_dir_result, q_fish_dir
    q_fish_pos = deque(fish_pos_result)
    q_shark_pos = deque(shark_pos_result)
    q_fish_dir = deque(fish_dir_result)
    shark_pos_result = []
    fish_pos_result = []
    fish_dir_result = []

def fish_copy_complete():
    global q_fish_pos_tmp, q_fish_dir_tmp, q_fish_pos, q_fish_dir
    # print(q_fish_pos, q_fish_pos_tmp) # deque([[3, 3], [0, 3], [0, 2], [1, 3]]) [[3, 2], [0, 2], [1, 3], [1, 0], [2, 3]]
    # print(q_fish_dir) # deque([4, 4, 1, 2])

    q_fish_pos.extend(q_fish_pos_tmp)
    q_fish_dir.extend(q_fish_dir_tmp)

    # print(q_fish_dir) # deque([4, 4, 1, 2, 4, 4, 1, 5, 3])
    # print(q_fish_pos) # deque([[3, 3], [0, 3], [0, 2], [1, 3], [3, 2], [0, 2], [1, 3], [1, 0], [2, 3]])


def solve():
    # global q_fish_pos, q_fish_dir
    # print(q_fish_pos, q_fish_dir)
    for _ in range(S):
        fish_copy()
        fish_move()
        shark_move()

        smelling()
        posing()

        fish_copy_complete()
        # print(q_fish_pos_tmp)
        # print(q_fish_dir, q_shark_pos, q_fish_pos)
    print(len(q_fish_pos))
solve()