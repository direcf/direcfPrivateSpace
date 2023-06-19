import sys
sys.stdin = open('number5.txt', 'r')
# 시간: 1시간 (10시20분~11시20분)
# 벽 또는 자기자신과 부딪치면 게임이 끝난다
# 처음 오른쪽 방향으로 이동
# 사과를 먹으면 길이 +1, 안 먹으면 이동
from collections import deque

# step0. input 받아오기
N = int(input())
A_N = int(input())
A_pos = []
for _ in range(A_N):  ###### (중요) 1행1열이 (0,0)이다...!
    temp = list(map(int, input().split()))
    A_pos.append([temp[0] - 1, temp[1] - 1])

M_N = int(input())
change_time = []
change_dir = []
for i in range(M_N):
    tmp = input().split()
    change_time.append(int(tmp[0]))
    change_dir.append(tmp[1])
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)  # 오른쪽, 아래, 왼쪽, 위


# step1. move 함수 만들기
def move(dir, q):
    global N
    x, y = q[0][0], q[0][1]  # cur position
    nx, ny = x + dx[dir], y + dy[dir]  # next position
    if 0 <= nx < N and 0 <= ny < N:  # 벽과 부딪치지 않는 조건
        if [nx, ny] not in q:  # 자기 자신과 만나지 않는 조건
            if [nx, ny] in A_pos:  # 다음이 사과인경우
                q.appendleft([nx, ny])  # 머리늘어나기
                A_pos.remove([nx, ny])  # 사과없애기
            else:  # 다음이 사과가 아닌경우
                q.appendleft([nx, ny])
                q.pop()
            return True, dir, q

    return False, dir, q


def solve():
    q = deque()
    q.append([0, 0])  # index 0이 머리 앞쪽이라고 생각하자
    cnt = 0
    dir = 0
    while True:  # 매초 진행
        # 방향전환
        if cnt in change_time:
            idx = change_time.index(cnt)
            if change_dir[idx] == 'D':
                dir = (dir + 1) % 4
            elif change_dir[idx] == 'L':
                dir = (dir + 3) % 4  # (중요) 왼쪽으로 가서 음수가 되면 case를 또 나눠야 한다 // 한번씩 변환하는 경우 괜찮다!!

        # 움직이기
        TF, dir, q = move(dir, q)
        cnt += 1

        if TF == False:
            break

    return print(cnt)


solve()