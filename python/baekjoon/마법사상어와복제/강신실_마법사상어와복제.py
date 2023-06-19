'''
start   7:37
end     
상어의 마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.
duplicate_fish()
1. 상어가 모든 물고기에게 복제 마법을 시전한다. 복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
move_fish()
2. 모든 물고기가 한 칸 이동한다. 
    상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
    각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수있는 칸을 향할 때 까지 방향을 45 도 반시계 회전시킨다.
    만약 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
    이외의 경우에는 그 칸으로 이동한다.
move_shark()
3. 상어가 연속해서 3칸 이동한다.
    상어는 현재 칸에서 상하좌우 인접한 칸으로 이동할 수 있다. 이동하는 중 격자 벗어나면 못간다. 
    이동중 물고기가 있는 칸에 가면 물고기는 격자에서 제외되고, 물고기 냄새를 남긴다.
    가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러개면 사전순으로 가장 앞서는 방법 쓴다.
    사전순이란 상은 1, 좌는 2, 하는 3, 우는 4로 변환
remove_smell()
4. 두번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
create_fish()
5. 1에서 사용산 복제마법 완료. 모든 물고기는 1에서 위치, 방향 그대로
'''
import pdb
from collections import defaultdict
import copy
# 상2 좌0 하6 우4
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
m, s = map(int,input().split())
fishes = []
board_smell = [[[False, False] for _ in range(4)] for _ in range(4)]
fishes_d = defaultdict(list)
for _ in range(m):
    r, c, d = map(int,input().split())
    fishes_d[(r-1,c-1)].append(d-1)
sr, sc = map(int,input().split())
shark = (sr-1, sc-1)
def move_fishes():
    '''
    2. 모든 물고기가 한 칸 이동한다. 
    상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
    각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수있는 칸을 향할 때 까지 방향을 45 도 반시계 회전시킨다.
    만약 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
    이외의 경우에는 그 칸으로 이동한다.
    '''
    global fishes_d, board_smell
    n_fishes_d = defaultdict(list)
    for r in range(4):
        for c in range(4):
            for i, fish_d in enumerate(fishes_d[(r,c)]):
                backup = fish_d
                num_dir_change = 0
                flag = False
                while num_dir_change<8:
                    nr = r + dr[fish_d]
                    nc = c + dc[fish_d]
                    if 0<=nr<4 and 0<=nc<4 and board_smell[nr][nc][0]==False and board_smell[nr][nc][1]==False and shark != (nr,nc):
                        n_fishes_d[(nr,nc)].append(fish_d)
                        flag = True
                        break
                    else:
                        fish_d = (fish_d-1)%8
                        num_dir_change +=1
                if num_dir_change == 7 and flag == False:
                    n_fishes_d[(r,c)].append(backup)
    fishes_d = n_fishes_d
                    
def move_shark(cnt, rm_fishes_list, sr, sc, candi):
    '''
    3. 상어가 연속해서 3칸 이동한다.
    상어는 현재 칸에서 상하좌우 인접한 칸으로 이동할 수 있다. 이동하는 중 격자 벗어나면 못간다. 
    이동중 물고기가 있는 칸에 가면 물고기는 격자에서 제외되고, 물고기 냄새를 남긴다.
    가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러개면 사전순으로 가장 앞서는 방법 쓴다.
    사전순이란 상은 1, 좌는 2, 하는 3, 우는 4로 변환
    DFS
    '''
    
    global fishes_d, max_rm_fishes, dr, dc, shark, v, n_shark
    def get_cnt(fl):
        ans = 0
        for r, c in list(fl):
            ans += len(fishes_d[(r,c)])
        return ans
    shark_d = [2,0,6,4]
    if cnt == 3:
        candi_cnt = get_cnt(rm_fishes_list)
        max_cnt = get_cnt(max_rm_fishes)
        if candi_cnt>max_cnt:
            max_rm_fishes = rm_fishes_list
            n_shark = [sr, sc]
            print("DFS", max_rm_fishes, candi)
    else:
        for d in range(4):
            nr = sr + dr[shark_d[d]]
            nc = sc + dc[shark_d[d]]
            if 0<=nr<4 and 0<=nc<4 :
                
                if v[nr][nc]==False and len(fishes_d[(nr,nc)])>0:
                    v[nr][nc]=True
                    backup_rm = copy.deepcopy(rm_fishes_list)
                    rm_fishes_list.add((nr,nc))
                    # pdb.set_trace()
                    move_shark(cnt+1, rm_fishes_list, nr, nc, candi + [d])
                    rm_fishes_list = backup_rm
                else:
                    if (nr,nc) not in candi:
                        move_shark(cnt+1, rm_fishes_list, nr, nc, candi+ [d])
                    else:
                        move_shark(cnt+1, rm_fishes_list, nr, nc, candi+ [d])
                v[nr][nc]=False


    

def print_fishes(fishes_d):
    for r in range(4):
        s = ''
        for c in range(4):
            
            s = s + str(fishes_d[(r,c)])+"\t"
        print(s)
def remove_smell(loc_list):
    # smell 을 없애고, fish를 없앤다
    global board_smell, fishes_d
    for r in range(4):
        for c in range(4):
            board_smell[r][c][1] = board_smell[r][c][0]
            board_smell[r][c][0] = False
    for r, c in loc_list:
        board_smell[r][c][0] = True
        fishes_d[(r,c)] = []
def create_fish():
    global backup_fishes, fishes_d
    for r in range(4):
        for c in range(4):
            fishes_d[(r,c)] = fishes_d[(r,c)] + backup_fishes[(r,c)]

def count_fishes():
    ans = 0
    global fishes_d
    for r in range(4):
        for c in range(4):
            ans += len(fishes_d[(r,c)])
    return ans
def print_board(b):
    for l in b:
        s = ''
        for e in l:
            s = s + str(e[0])+"\t"
        print(s)
    print("="*10)
    for l in b:
        s = ''
        for e in l:
            s = s + str(e[1])+"\t"
        print(s)
for ii in range(s):
    if ii == 3:
        pdb.set_trace()
    # duplicate_fish
    
    backup_fishes = copy.deepcopy(fishes_d)
    print("MOVE FISH")
    move_fishes()
    print_fishes(fishes_d)
    max_rm_fishes = []
    n_shark = []
    print("MOVE SHARK")
    v = [[False for _ in range(4)] for _ in range(4)]
    n_shark = []
    pdb.set_trace()
    move_shark(0, set(), list(shark)[0], list(shark)[1], [])
    shark = set(n_shark)
    print("shark", shark)
    print("remove fish", max_rm_fishes)
    remove_smell(max_rm_fishes)
    print("SMELL BOARD")
    print_board(board_smell)

    print_fishes(fishes_d)
    create_fish()
    print(ii, "CREATE FISH")
    print_fishes(fishes_d)

print(count_fishes())

