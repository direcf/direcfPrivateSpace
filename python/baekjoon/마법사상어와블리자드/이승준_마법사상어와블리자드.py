# 시간: 18시20분~20시10분
import sys
sys.stdin = open('number22.txt','r')

def print_board(a):
    for b in a:
        s = ''
        for c in b:
            s = s + str(c) + ' '
        print(s)

# check1. 격자의 가장 위가 1이기 때문에 -1 필요
# check2. 마법사 상어 위치 (N//2, N//2)

# step1. 구슬 던지기 -> 이
# step2. 구슬 폭발(4개연속) -> 이동 [반복] (폭발한 갯수를 출력)
# step3. 구슬 변화 [갯수, 숫자]

# N은 홀수 3 ≤ N ≤ 49  1 ≤ M ≤ 100
N, M = map(int, input().split())
dx, dy = (0,1,0,-1), (-1,0,1,0)
board = []
last_answer = [0,0,0]
for _ in range(N):
    board.append(list(map(int, input().split())))

def change_board():
    global line_list
    x, y = N//2, N//2
    line_tmp = []
    line_tmp.append(board[x][y])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    dir = 0

    # (중요!) [0,0]에 도달하면 끝내는 걸로 while문 만들 수 있겠다
    while True:
        # print(x,y,dir)
        if x == 0 and y == 0:
            break
        nx, ny = x+dx[dir], y+dy[dir]

        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] == False:
                dir = (dir + 1) % 4
                visited[nx][ny] = True
                x, y = nx, ny
                line_tmp.append(board[nx][ny])
            elif visited[nx][ny] == True: #### (중요!) 이것떄문에 시간 10분 소모...!
                dir = (dir + 3) % 4

    line_list = [i for i in line_tmp if i != 0]

def destroy_ball(direction, distance):
    global line_list
    if direction == 1:
        num = 6
        for i in range(distance):
            line_list[num] = 0
            num += (7 + 8 * (i+1))

    elif direction == 2:
        num = 2
        for i in range(distance): # 0, 1
            line_list[num] = 0
            num += (3 + 8 * (i+1))

    elif direction == 3:
        num = 0
        for i in range(distance):
            line_list[num] = 0
            num += (1 + 8 * (i+1))

    elif direction == 4:
        num = 4
        for i in range(distance):
            line_list[num] = 0
            num += (5 + 8 * (i+1))

    # print(line_list)
    # exit(0)
    # # 0인 부분은 모두 제거하기
    line_list = [i for i in line_list if i != 0]

import copy
def explode_ball():
    global line_list, last_answer
    start = 0
    while True:
        stack = []
        index_list = []
        # print("step1", line_list)
        for i in range(start, len(line_list)): # (중요!!) len(line_list)는 계속변한다!
            # print(stack, start, prev_num)
            if len(stack) == 0:
                stack.append(line_list[i])
                index_list.append(i)
            else:
                if stack[-1] == line_list[i]:
                    index_list.append(i)
                    # stack.append(line_list[i])
                else:
                    if len(index_list) >= 4: # 제거되는 경우
                        last_answer[line_list[index_list[0]] - 1] += len(index_list) # (중요!) 더 효율성있게 만드는 방법 고민필요!
                        for idxx in index_list:
                            line_list[idxx] = 0


                        line_list = [i for i in line_list if i != 0]
                        start = 0
                        break
                    else:
                        start = i
                        break

            if i == len(line_list)-1:
                # print(len(line_list))
                return

def change_ball():
    global line_list

    new_line_list = []
    stack = []
    for i in range(len(line_list)):
        if i == 0:
            cnt = 1
            stack.append(line_list[i])
        else:
            if stack[-1] == line_list[i]:
                cnt += 1

            else: # 새로운 원소가 들어왔을 때
                new_line_list.extend([cnt, stack[-1]])
                stack.append(line_list[i])
                cnt = 1
    new_line_list.extend([cnt, stack[-1]])
    line_list = new_line_list
    # print(new_line_list)
    # print(len(new_line_list))


def solve():
    change_board()
    for _ in range(M):
        d, s = map(int, input().split())
        destroy_ball(d, s)
        explode_ball() # 시간: 19시 52분         # print(last_answer) # [5, 4, 5]
        change_ball() # 시간: 20시 05분

    score = 0
    for index, answer in enumerate(last_answer):
        score += (index+1) * answer
    print(score)
    # 시간초과 발생
solve()