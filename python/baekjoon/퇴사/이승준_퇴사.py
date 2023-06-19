# 핵심: dfs를 이용
# 시간: 30분
import sys
sys.stdin = open('number2.txt', 'r')
N = int(input())
time_cost = []
for _ in range(N):
    time_cost.append(list(map(int, input().split())))

max_value = 0

def dfs(start, cur_cost):
    global max_value, time_cost, N

    for index in range(start, N):
        if time_cost[index][0] + index <= N:
            cur_cost += time_cost[index][1] # [start]가 아닌 [index]
            dfs(index+time_cost[index][0], cur_cost)
            cur_cost -= time_cost[index][1]

    max_value = max(max_value, cur_cost)
    return

def solve():
    for idx in range(N):
        cur_cost = 0
        dfs(idx, cur_cost)
    print("max:", max_value)


solve()