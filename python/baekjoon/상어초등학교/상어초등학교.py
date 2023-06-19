import sys
sys.stdin = open('number12.txt')
# 시간: 20시30분~21시20분

# (check) 1행1열부터 시작하므로 빼줘야 한다 ()

# 조건1) 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 조건2) 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 조건3) 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 고민1) dict이 좋을까? 한꺼번에가 좋을까? student num과 liked list를 나누느게 좋을까?
# >> dict으로 도전!
from collections import defaultdict
N = int(input()) # 3 ≤ N ≤ 20
board = [[0] * N for _ in range(N)]
student_dict = defaultdict(list)

for _ in range(N*N):
    tmp = list(map(int, input().split()))
    student_dict[tmp[0]] = tmp[1:]
# print(student_dict) # defaultdict(<class 'list'>, {4: [2, 5, 1, 7], 3: [1, 9, 4, 5], 9: [8, 1, 2, 3], 8: [1, 9, 3, 4], 7: [2, 3, 4, 8], 1: [9, 2, 5, 7], 6: [5, 2, 3, 4], 5: [1, 9, 2, 8], 2: [9, 3, 1, 4]})

dx,dy = (1,0,-1,0),(0,1,0,-1)
def sitting():
    # 고민2. 4중 for문이 나오는데 이게 맞나?...
    for k, v in student_dict.items():
        like_num_list = []
        empty_num_list = []
        cur_pos_list = []
        # x,y는 현재 포지션
        for x in range(N):
            for y in range(N):
                if board[x][y] == 0: # 현재 위치가 빈 공간이라 앉을 수 있어야 한다
                    # 탐색전 빈공간 count
                    cur_pos_list.append([x,y])
                    empty_cnt = 0
                    like_cnt = 0
                    # i는 방향에 대한 탐색
                    for i in range(4):
                        nx, ny = x+dx[i], y+dy[i]
                        if 0<=nx<N and 0<=ny<N: # 격자내에 위치하는지 확인
                            if board[nx][ny] == 0:
                                empty_cnt += 1
                            elif board[nx][ny] in v:
                                like_cnt += 1

                    empty_num_list.append(empty_cnt)
                    like_num_list.append(like_cnt)
                    # print(empty_num_list, like_num_list, cur_pos_list)

        # like_num_list 비교 (너무 비효율적인 비교라고 생각된다...)
        max_val = max(like_num_list)
        max_cnt = like_num_list.count(max_val)
        if max_val == 0:
            pass
        elif max_cnt > 1:
            index1 = [idx for idx, i in enumerate(like_num_list) if i == max_val]
            cur_pos_list = [i for idx, i in enumerate(cur_pos_list) if idx in index1]
            like_num_list = [i for idx, i in enumerate(like_num_list) if idx in index1]
            empty_num_list = [i for idx, i in enumerate(empty_num_list) if idx in index1]
        else: # 1개인 경우
            tmp_pos = cur_pos_list[like_num_list.index(max_val)]
            board[tmp_pos[0]][tmp_pos[1]] = k
            continue

        max_val = max(empty_num_list)
        max_cnt = empty_num_list.count(max_val)
        if max_cnt > 1:
            index1 = [idx for idx, i in enumerate(empty_num_list) if i == max_val]
            cur_pos_list = [i for idx, i in enumerate(cur_pos_list) if idx in index1]
            like_num_list = [i for idx, i in enumerate(like_num_list) if idx in index1]
            empty_num_list = [i for idx, i in enumerate(empty_num_list) if idx in index1]
        else:
            tmp_pos = cur_pos_list[empty_num_list.index(max_val)]
            board[tmp_pos[0]][tmp_pos[1]] = k
            continue
        board[cur_pos_list[0][0]][cur_pos_list[0][1]] = k
        # print(cur_pos_list,"AAAA", empty_num_list," BBBB", like_num_list)

result = 0
def calc_happiness():
    global board, student_dict,result
    for x in range(N):
        for y in range(N):
            cnt = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if board[nx][ny] in student_dict[board[x][y]]:
                        cnt +=1
            if cnt == 0:
                result += 0
            elif cnt == 1:
                result += 1
            elif cnt == 2:
                result += 10
            elif cnt == 3:
                result += 100
            elif cnt == 4:
                result += 1000
    print(result)

def solve():
    sitting()
    calc_happiness()

solve()


