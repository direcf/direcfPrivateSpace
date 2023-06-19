import sys
sys.stdin = open('number7.txt', 'r')

import copy
N,M,K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# print(board)

from collections import defaultdict
tree_info = defaultdict(list)
for _ in range(M):
    tmp = list(map(int, input().split()))
    tree_info[(tmp[0]-1, tmp[1]-1)].append(tmp[2]) 
base = [[5] * N for _ in range(N)]
# print(base)

dx, dy = (1,1,0,-1,-1,-1,0,1), (0,-1,-1,-1,0,1,1,1)

def solve():
    for kk in range(K):
        dead_tree_info = defaultdict(list)
        # 봄
        for k,v in tree_info.items():
            tree_info[k].sort()
            tree_info_tmp = copy.deepcopy(tree_info)
            for tree_age in tree_info_tmp[k]:
                if base[k[0]][k[1]] >= tree_age: # 양분 >= 나이
                    base[k[0]][k[1]] -= tree_age
                else: # 양분이 적은 경우
                    dead_tree_info[(k[0],k[1])].append(tree_age)
                    tree_info[k].remove(tree_age)

            # 나이 1씩 먹기
            for index in range(len(tree_info[k])):
                tree_info[k][index] += 1


        # 여름
        for k,v in dead_tree_info.items():
            for tree_age in dead_tree_info[k]:
                base[k[0]][k[1]] += (tree_age // 2)

        # 가을
        tree_info_tmp = copy.deepcopy(tree_info)
        for k,v in tree_info_tmp.items(): # RuntimeError: dictionary changed size during iteration
            cnt = 0
            for age in tree_info[k]:
                if age % 5 == 0:
                    cnt += 1
            if cnt == 0:
                continue
            # cnt가 0이 아닌 경우에만
            x, y = k[0], k[1] # 기준점
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N: # 범위 벗어나지 않는지 체크
                    for _ in range(cnt):
                        tree_info[(nx,ny)].append(1)

        # 겨울
        for i in range(N):
            for j in range(N):
                base[i][j] += board[i][j]
    # 나무의 갯수 마지막으로 count
    answer = 0
    for k,v in tree_info.items():
        answer += len(tree_info[k])

    return print(answer)

solve()