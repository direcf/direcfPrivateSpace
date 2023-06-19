import sys
sys.stdin = open('number35.txt','r')
def print_board(a):
    for b in a:
        s = ''
        for c in b:
            s = s + str(c) + ' '
        print(s)
    print()

# (step1) 냄새뿌리기
# >> smell_dict (x,y) [shark_num,K-i]  >> (중요!) dict내에 dict을 만들 수는 없을까?...

# (step2) 1초마다 동시에 이동
# >> 냄새는 상어가 K번 이동하면 사라진다
# >> 냄새가 없는 곳 > 자기가 뿌린 냄새
# >> 가능한 칸이 여러개일 경우, 바라보고 있는 방향에 따른 각자의 우선순위를 따른다
# >> shark_num이 바뀌는 경우는 없으니까 우선순위는 list형태로 만들어도 좋을 것 같다

# (step3) 한 칸에 여러상어가 있을 경우, 가장 번호가 작은 상어 제외 모두 쫓아낸다
# >> shark_dict (x,y) [shark_num, dir]
# >> for k,v in a.items():
# >>    if len(v) > 1:
# >>        a[k] = v[0]
from collections import defaultdict
N, M, K = map(int, input().split())
tmp_board = []
for _ in range(N):
    tmp_board.append(list(map(int, input().split())))
tmp_dir = list(map(int, input().split()))
shark_dict = defaultdict(list)
smell_dict = defaultdict(list)
for i in range(N):
    for j in range(N):
        if tmp_board[i][j] > 0:
            tmp_num = tmp_board[i][j]-1
            shark_dict[(i,j)].append([tmp_num, tmp_dir[tmp_num]-1])
# print(shark_dict) # defaultdict(<class 'list'>, {(0, 4): [[2, 2]], (1, 1): [[1, 3]], (2, 0): [[0, 3]], (2, 4): [[3, 0]]})
priority_list =  []
for _ in range(M):
    priority_list.append([])
    for _ in range(4):
        tmp_list2 = list(map(int, input().split()))
        priority_list[-1].append([tmp_list2[0]-1, tmp_list2[1]-1, tmp_list2[2]-1, tmp_list2[3]-1])
# print(priority_list[0]) # [[1, 2, 0, 3], [3, 0, 1, 2], [2, 3, 1, 0], [3, 2, 0, 1]]
dx, dy = (-1,1,0,0), (0,0,-1,1)

def left_smell(): # 냄새의 count를 해주는건 움직임이후
    global shark_dict, smell_dict
    for k, v in shark_dict.items():
        if k in smell_dict.keys():
            smell_dict[k] = [v[0][0], K - 1]
        else:
            smell_dict[k].extend([v[0][0],K-1]) #### (중요!) 이거 바꿔주기


def move_shark(): # 동시에 움직인다는 사실에 입각해서 생각해보자
    global shark_dict, smell_dict
    new_shark_dict = defaultdict(list)
    # (중요!) 여기서 sorted하는 이유는 번호가 큰 상어부터 움직여서 append가 아닌 =로 해서 잡아먹는걸 만들기 위해서


    for shark_info in sorted(shark_dict.items(), key=lambda x: -x[1][0][0]):
        x, y = shark_info[0][0], shark_info[0][1]
        sw = 0
        # 냄새가 아닌 빈공간인지 여부
        for diro in priority_list[shark_info[1][0][0]][shark_info[1][0][1]]:
            nx, ny = x + dx[diro], y + dy[diro]
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in smell_dict.keys():
                    new_shark_dict[(nx, ny)] = [[shark_info[1][0][0],diro]]
                    sw = 1
                    break
        if sw == 1:
            continue

        # 자기 냄새의 칸 중 우선순위에 부합하는 곳으로 이동
        for diro in priority_list[shark_info[1][0][0]][shark_info[1][0][1]]:
            nx, ny = x + dx[diro], y + dy[diro]
            if 0 <= nx < N and 0 <= nx < N:
                if (nx, ny) in smell_dict.keys():
                    tmp_info = smell_dict[(nx, ny)]
                    # print(tmp_info, shark_info)
                    if tmp_info[0] == shark_info[1][0][0]:
                        new_shark_dict[(nx, ny)] = [[shark_info[1][0][0],diro]]
                        break

    shark_dict = new_shark_dict


def decrease_smell():
    global smell_dict
    new_smell_dict = defaultdict(list)
    for k,v in smell_dict.items():
        if v[1] == 0:
            continue
        else:
            new_smell_dict[k] = [v[0],v[1]-1]
    smell_dict = new_smell_dict

def solve():
    STEP = 0
    while STEP < 1000:
        STEP += 1
        # print("STEP", STEP)

        # print("BEFORE SHARK",shark_dict)
        left_smell()
        # print("SEMLL", smell_dict)

        move_shark()
        # print("AFTER MOVE",shark_dict)
        decrease_smell()
        # print("SEMLL", smell_dict)

        if len(shark_dict.keys()) == 1:
            break
    if STEP == 1000:
        print(-1)
        return #### (중요!) 여기서 exit(0)을 써버리면 다른 test case들이 돌아가지 못하고 종료되어 버린다
    print(STEP)

    # 문제점 찾았다! (1, 1): [1, 3, 1, 5] >> (1,1): [1, 5]로 냄새 update시켜야 한다

solve()