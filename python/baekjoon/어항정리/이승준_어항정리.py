# 시간: 20시10분~
import sys
sys.stdin = open('number23.txt','r')

N, K = map(int, input().split()) # N은 4의 배수 // 최대최소 차이가 K이하가 되게 만들려면 몇번!
line_list = list(map(int, input().split()))

# idea1. N에 따라 회전하는 횟수파악: 4(2), 8(4), 12(5), 16(6), 20(7)... 규칙을 찾기 어려움..
# idea2. 직접 모든 프로세스를 수행하게 만들어야 한다 (0 1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7...)
# >> 굳이 몇 번 해야하는지 파악할 필요x >> while 문으로 구성해야 한다.
# 아니다! idea1이 맞는 방법이다 다른 방법으로 하면 너무 복잡하자.

# step1. N을 넣었을 때, 숫자가 회전 갯수가 나오도록 짜자
dx, dy = (1,0,-1,0), (0,-1,0,1)
def rot_times():
    global rot_time
    rot_time = [0, 1]
    num = 1
    cnt = 2
    while len(rot_time) < 101:
        num += 1
        for _ in range(cnt):
            rot_time.append(num)
        num += 1
        for _ in range(cnt):
            rot_time.append(num)
        cnt += 1

def board_create():

    board_length = 0
    for i in range(10):
        if i*i >= N:
            board_length = i
            break
    return board_length

import copy
def solve():


    # step1. 방향설정
    rot_times()
    dir_ori = (rot_time[N] - 1) % 4  # N=8일 때, 3방향인 오른쪽으로

    # step2. 넣을 board 만들기
    board_length = board_create()

    cnt = 0
    while True:
        cnt += 1

        dir = dir_ori
        board = [[0] * board_length for _ in range(board_length)]
        visited = [[False] * board_length for _ in range(board_length)]

        # step3. 방향순서대로 search 하면서 값 넣기
        if board_length % 2 == 0:
            sx, sy = board_length // 2 - 1, board_length // 2 - 1
        elif board_length % 2 == 1:
            sx, sy = board_length // 2, board_length // 2
        visited[x][y] = True
        for ele in line_list:


solve()