# 7:35-
# 1:37.
from collections import deque
n,q = map(int,input().split())
board =[]
n = 3
board_len = 2<<(n-1)
for i in range(board_len):
    board.append(list(map(int, input().split())))


dx = [-1,+1,+0,+0]
dy = [+0,+0,-1,+1]

def second():
    global board_len
    for i in range(board_len):
        for j in range(board_len):
            cnt = 0
            for k in range(4):
                cur_x = j + dx[k]
                cur_y = i + dy[k]
                if cur_x > 0 and cur_x < board_len and cur_y > 0 and cur_y < board_len and board[cur_y][cur_x] <= 0:
                    cnt += 1
            if cnt >= 3:
                board[i][j] += -1


for magic in map(int, input().split()):
    new_list = [[] for _ in range(board_len)]
    magic = 2<<(magic-1)
    magic_list = []
    for i in range(1, board_len+1):
        if i % magic != 0:
            magic_list.append(board[i-1])
        else:
            magic_list.append(board[i-1])
            magic_list2 = [[] for _ in range(magic)]
            for j in range(board_len):
                if (j+1) % magic != 0:
                    for k in range(i-magic, i):
                        magic_list2[k-(i-magic)].append(board[k][j])
                else:
                    for k in range(i-magic, i):
                        magic_list2[k-(i-magic)].append(board[k][j])
                    # 매직 실시 + 새로운 배열에 넣기. 1/4
                    magic_fin_list = list(zip(*list(reversed(magic_list2))))
                    for k in range(i - magic, i):
                        for v in magic_fin_list[k - (i - magic)]:
                            new_list[k].append(v)
                    magic_list2 = [[] for _ in range(magic)]
            # 다 정리된 new_arr를 다시 넣는다. 4/4
            magic_list = []

    board = new_list

    # 2. 인전 얼음양 1 줄어드는 식
    second()

# 1. 합
ans = 0
for i in range(board_len):
    ans += sum(board[i])
print(ans)

# 2. 덩어리
qu = deque()
qu.append((0,0,board[0][0]))
visited = [[0] for _ in range(board_len)] * board_len
max_ans = 0
while qu:
    cur = qu.popleft()
    y = cur[0]
    x = cur[1]
    cur_sum = cur[2]
    if visited[y][x] == -1:
        pass
    else:
        for i in range(4):
            cur_y = y + dy[i]
            cur_x = x + dx[i]
            if cur_x > 0 and cur_x < board_len and cur_y > 0 and cur_y < board_len:
                if visited[cur_y][cur_x] == 0:
                    cur_sum += board[cur_y][cur_x]
                    visited[cur_y][cur_x] = -1
                    qu.append((cur_y, cur_x, cur_sum))

        max_ans = max(max_ans, cur_sum)

print(max_ans)






# 3 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2 3 4 5 6 7 8 9
# 8 7 6 5 4 3 2 1
# 3 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 4 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1

# 3 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2 3 4 5 6 7 8 9
# 8 7 6 5 4 3 2 1
# 3 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 4 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2