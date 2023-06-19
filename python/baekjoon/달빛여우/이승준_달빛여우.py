# 시간: 20시48분~

import sys
sys.stdin = open('number5.txt','r')

from collections import defaultdict
N, M = map(int, input().split())
info = []
node_dict = defaultdict(list)
edge_dict = defaultdict(list)
for _ in range(M):
    info = list(map(int, input().split()))
    node_dict[info[0]-1].append(info[1]-1)
    node_dict[info[1]-1].append(info[0]-1)
    edge_dict[info[0]-1].append(info[2])
    edge_dict[info[1]-1].append(info[2])

# print(node_dict) # defaultdict(<class 'list'>, {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 4], 3: [1], 4: [2]})
# print(edge_dict) # defaultdict(<class 'list'>, {0: [3, 2], 1: [3, 2, 4], 2: [2, 2, 4], 3: [4], 4: [4]})

route_dict = defaultdict(list)

visited = [False] * N
def dfs(start, end, route):
    if start == end:
        route_dict[end].append(route)
        return

    for i in node_dict[start]:
        if visited[start] == False:
            visited[start] = True
            dfs(i, end, route+[i])
            visited[start] = False

for i in range(N-1):
    dfs(0, i+1, [0])

answer = 0
for k, v in route_dict.items():
    min_fox = int(1e9) # fox
    min_wolf = int(1e9) # wolf
    for paths in v:
        fox = 0
        wolf = 0
        # print(paths)
        for idx, path  in enumerate(paths):
            if len(paths) - 1 > idx:
                idxx = node_dict[paths[idx]].index(paths[idx+1])
                time = edge_dict[paths[idx]][idxx]
                if idx % 2 == 0: # 짝수
                    fox += time / 1
                    wolf += time / 2
                elif idx % 2 == 1: # 홀수
                    fox += time / 1
                    wolf += time * 2
                # print(fox, wolf)
                # print()
        min_fox = min(min_fox, fox)
        min_wolf = min(min_wolf, wolf)
        # print(min_fox, min_wolf)
    if min_fox < min_wolf:
        answer += 1
print(answer)