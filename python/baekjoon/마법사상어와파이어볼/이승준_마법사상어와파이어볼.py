# 시간: 11시32분~12시20분(48분)
import sys
sys.stdin = open('number33.txt')

from collections import defaultdict
import copy
N, M, K = map(int, input().split()) # N은 격자크기, M은 처음 파이어볼 갯수, K는 이동명령횟수
dx, dy = (-1,-1,0,1,1,1,0,-1), (0,1,1,1,0,-1,-1,-1)
tmp_board = []
fireball_dict = defaultdict(list)
for _ in range(M):
    tmp_board = list(map(int, input().split()))
    fireball_dict[(tmp_board[0]-1,tmp_board[1]-1)].append([tmp_board[2],tmp_board[3],tmp_board[4]]) 

def solve():
    global fireball_dict
    for _ in range(K):
        tmp_fireball_dict = defaultdict(list)  
        # step1. 파이어볼 이동
        for k, v_zip in fireball_dict.items():
            for v in v_zip:
                nx, ny = (k[0]+dx[v[2]] * v[1]) % N , (k[1]+dy[v[2]] * v[1]) % N
                tmp_fireball_dict[(nx,ny)].append(v)

        # step2. 파이어볼 합쳐지고 나눠지기
        fireball_dict2 = defaultdict(list) 
        for k, v_zip in tmp_fireball_dict.items():
            if len(v_zip) == 1:
                fireball_dict2[k].extend(v_zip)
            elif len(v_zip) >= 2:
                total_mass = 0
                total_speed = 0
                odd_even = [0,0] # 짝, 홀
                fireball_num = len(v_zip)
                for v in v_zip:
                    total_mass += v[0]
                    total_speed += v[1]
                    if v[2] % 2 == 0:
                        odd_even[0] += 1
                    else:
                        odd_even[1] += 1

                if total_mass // 5 == 0:
                    continue
                else:
                    each_mass = total_mass // 5
                    each_speed = total_speed // fireball_num
                    if 0 in odd_even:
                        dir_zip = [0,2,4,6]
                    else:
                        dir_zip = [1,3,5,7]

                    for new_dir in dir_zip:
                        fireball_dict2[k].append([each_mass, each_speed, new_dir])
        fireball_dict = copy.deepcopy(fireball_dict2) # (중요!) 이거 indentation 때문에..

    left_mass = 0
    for k, v_zip in fireball_dict.items():
        for v in v_zip:
            left_mass += v[0]
    print(left_mass)


solve()