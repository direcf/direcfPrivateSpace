# 시간:12시10분~13시30분
import sys
sys.stdin = open('number15.txt','r')

# step1. 낚시꾼이 오른쪽으로 이동하면서 가장 가까운쪽 줄에 있는 상어를 잡아먹는다
# step2. 상어의 이동
# step3. 상어의 이동이 끝난 후, 같은 칸에 있는 상어끼리 잡아먹는다

from collections import defaultdict
import copy
R,C,M = map(int, input().split())

# (중요!) sorted는 받아주는 값이 필요하다...!!!
# shark_info = []
# for _ in range(M):
#     tmp = list(map(int, input().split()))
#     shark_info.append([tmp[0]-1, tmp[1]-1, tmp[2], tmp[3]-1, tmp[4]])
# print(shark_info)
# shark_info = sorted(shark_info, key=lambda x: x[1]) # 받아줘야 하는구나...!!!!!
# print(shark_info)

dx, dy = (-1,1,0,0), (0,0,1,-1)
# dx, dy = (-1,0,1,0),(0,1,0,-1) # 위,아래,오른쪽,왼쪽 # (위,오른쪽,아래,왼쪽)
# (check) dictionary로 같이 움직이면 편한데...이렇게는 안 되는건가??
shark_dict = defaultdict(list)
for _ in range(M):
    tmp = list(map(int, input().split()))
    shark_dict[(tmp[0] - 1, tmp[1] - 1)].append([tmp[2]])
    shark_dict[(tmp[0] - 1, tmp[1] - 1)][-1].append(tmp[3]-1) # 이동방향1~4이기 때문에 -1 해줬다
    shark_dict[(tmp[0] - 1, tmp[1] - 1)][-1].append(tmp[4])
#### (중요!!!) 낮은열, 낮은행 (dictionary tuple의 경우 sort가 불가능한가?..)
# shark_dict = sorted(shark_dict.items(), key=lambda x: [x[0][1],x[0][0]]) # [((2, 0), [1, 1, 1]), ((3, 0), [3, 2, 8]), ((1, 1), [2, 2, 5]), ((0, 2), [5, 1, 9]), ((2, 2), [1, 1, 7]), ((1, 3), [8, 3, 1]), ((0, 4), [8, 3, 3]), ((3, 4), [0, 0, 4]), ((2, 5), [2, 0, 2])]
new_shark_dict = defaultdict(list)
#### (중요!!) 이렇게 해야 dict to dict이 되는구나...!
for k,v in sorted(shark_dict.items(), key=lambda x: [x[0][1],x[0][0]]):
    new_shark_dict[k] = v


def move_shark():
    global shark_dict
    my_shark_dict = defaultdict(list)
    for pos, v in shark_dict.items():
        for real_val in v:
            cnt = 0
            x, y = pos[0], pos[1]
            dir = real_val[1]
            while True:
                if cnt == real_val[0]:
                    break
                nx,ny = x+dx[dir], y+dy[dir]

                if 0<=nx<R and 0<=ny<C:
                    x, y = nx, ny
                    cnt += 1
                else:
                    if dir == 0:
                        dir += 1
                    elif dir == 1:
                        dir -= 1
                    elif dir == 2:
                        dir += 1
                    elif dir == 3:
                        dir -= 1
                    # dir = (dir+2) % 4 # (중요!!!) 방향이 위,아래,오른,왼 순이면 안 된다...!
            # 이동이 끝나면 새로운 dict에 update
            my_shark_dict[(x,y)].append([real_val[0],dir,real_val[2]]) # 위치랑 방향만 update
    # print("move shark", my_shark_dict)
    shark_dict = copy.deepcopy(my_shark_dict)


shark_dict = copy.deepcopy(new_shark_dict)
for col in range(C):
    print("STEP", col)

    print("first line", shark_dict)
    new_shark_dict = copy.deepcopy(shark_dict)
    # step1. 낚시왕이 상어 잡아먹기
    for k,v in new_shark_dict.items():
        # print(col, k[1])
        if col == k[1]:
            x = shark_dict[k].pop()
            print("xxxx", x)
            if len(shark_dict[k]) == 0:
                del shark_dict[k]
            break

    # step2. 상어 움직이기
    print("original pos", shark_dict)
    move_shark()

    # step3. 상어끼리 잡아먹기
    print("moved", shark_dict)
    new_my_dict = defaultdict(list)
    for k,v in shark_dict.items():
        if len(v) > 1:
            v = sorted(v, key= lambda x: -x[2])
            # print(v[0]) #### (중요) 맞추기
            new_my_dict[k].append(v[0])
        else:
            # print(v)
            new_my_dict[k].extend(v)
    print("eating", new_my_dict)

    print()



