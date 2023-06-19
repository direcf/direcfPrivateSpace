# (r, c) - 1 based
# 처음에는 모든 칸이 0
# 1. 모든 온풍기에서 바람이 한 번
# 하드코딩?
# 같은 칸에 '같은' 온풍기에서 나온 바람이 여러 번 도착해도 온도는 한 번만 상승 (먼저 것만)
# 온풍기가 여러 대라면 상승한 값을 모두 합한 값이 최종 반영
# 온풍기가 있는 칸도 온도 상승 가능
# 벽
# 2. 온도 조절
# 높은 칸에서 낮은 칸으로
# [(높은 칸 - 낮은 칸 온도)/4] (1.5 -> 1.0)
# 높은 칸은 이 값만큼 낮아지고, 낮은 칸은 이 값만큼 높아짐
# 벽 있으면 온도 안 바뀜
# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 4. 초콜릿 하나 먹기
# 5. 조사하는 모든 칸의 온도가 K 이상인지? 맞다면 테스트 중단, 아니면 1부터 다시 시작

# 0: 빈 칸
# 1: ->
# 2: <-
# 3: 위
# 4: 아래
# 5: 조사 칸

#        (x-1, y)
#           ㅡ
# t: 0 -> (x, y)

# t: 1 -> (x, y)   | (x, y+1)

# 1 방향 온풍기 기준

wind = [
    (0, 1, 5),
    (-1, 2, 4), (0, 2, 4), (1, 2, 4),
    (-2, 3, 3), (-1, 3, 3), (0, 3, 3), (1, 3, 3), (2, 3, 3),
    (-3, 4, 2), (-2, 4, 2), (-1, 4, 2), (0, 4, 2), (1, 4, 2), (2, 4, 2), (3, 4, 2),
    (-4, 5, 1), (-3, 5, 1), (-2, 5, 1), (-1, 5, 1), (0,
                                                     5, 1), (1, 5, 1), (2, 5, 1), (3, 5, 1), (4, 5, 1)
]

def applied(item: tuple, amt: int):
    return (item[0]+amt, item[1])


def pnt(board):
    for row in board:
        print(row)
    print()


def blow(r, c, dir):
    "r, c 위치에서 dir 방향으로"
    global wind, board

    if dir == 1:   # -> 1
        local_wind = wind[:]
        validSet = [(0, -1, 0, 0), (0, -1, -1, -1), (0, -1, 1, -1)]
    elif dir == 2:  # <- 2
        local_wind = [(dr, -dc, amt) for dr, dc, amt in wind]
        validSet = [(0, 1, 0, 0), (0, 1, 1, 1), (0, 1, -1, 1)]
    elif dir == 3:  # 위 3
        local_wind = [(-dc, dr, amt) for dr, dc, amt in wind]
        validSet = [(-1, 0, 0, 0), (-1, 0, -1, -1), (-1, 0, -1, 1)]
    else:          # 아래 4
        local_wind = [(dc, dr, amt) for dr, dc, amt in wind]
        validSet = [(1, 0, 0, 0), (1, 0, 1, 1), (1, 0, 1, -1)]

    for dr, dc, amt in local_wind:
        notValid = False
        nr = r + dr
        nc = c + dc
        if oob(nr, nc):
            continue
        for vs in validSet:
            t, y, u, i = vs[0]+nr, vs[1]+nc, vs[2]+nr, vs[3]+nc
            if not valid(t, y, u, i):
                notValid = True
                break
        if notValid:
            continue

        board[nr][nc] = applied(board[nr][nc], amt)


def valid(r, c, nr, nc):
    global walls
    temp = [(r, c), (nr, nc)]
    temp.sort(key=lambda x: (x[0], x[1]))
    return temp not in walls


def oob(r, c):
    global R, C
    return not (0 <= r < R and 0 <= c < C)


def controlOutsideTemperature():
    global board

    if board[0][0][0] > 0:
        board[0][0] = applied(board[0][0], -1)
    if board[R-1][C-1][0] > 0:
        board[R-1][C-1] = applied(board[R-1][C-1], -1)
    if board[R-1][0][0] > 0:
        board[R-1][0] = applied(board[R-1][0], -1)
    if board[0][C-1][0] > 0:
        board[0][C-1] = applied(board[0][C-1], -1)

    for c in range(1, C-1):
        if board[0][c][0] > 0:
            board[0][c] = applied(board[0][c], -1)
    for r in range(1, R-1):
        if board[r][0][0] > 0:
            board[r][0] = applied(board[r][0], -1)
    for c in range(1, C-1):
        if board[R-1][c][0] > 0:
            board[R-1][c] = applied(board[R-1][c], -1)
    for r in range(1, R-1):
        if board[r][C-1][0] > 0:
            board[r][C-1] = applied(board[r][C-1], -1)


def terminate(candidates) -> bool:
    global K, board
    for r, c in candidates:
        if board[r][c][0] < K:
            break
    else:
        return True
    return False


def getCandidates() -> list:
    global board
    ret = []
    for r in range(R):
        for c in range(C):
            if board[r][c][1] == 5:
                ret.append((r, c))
    return ret


def controlTemperature():
    global board, R, C
    temp = [row[:] for row in board]
    for r in range(R):
        for c in range(C):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if oob(nr, nc):
                    continue
                if board[r][c][0] <= board[nr][nc][0]:
                    continue
                if not valid(r, c, nr, nc):
                    continue
                diff = board[r][c][0] - board[nr][nc][0]
                temp[r][c] = applied(temp[r][c], -(diff//4))
                temp[nr][nc] = applied(temp[nr][nc], diff//4)
    board = [row[:] for row in temp]


def dfs(r, c, dir):
    dirs = [(0, 1), (1, 1), (-1, 1)]
    if dir == 1:
        c += 1
        dirs = [(0, 1), (1, 1), (-1, 1)]
        validSet = [(0, -1, 0, 0), (0, -1, -1, -1), (0, -1, 1, -1)]
    elif dir == 2:
        c -= 1
        dirs = [(r, -c) for r, c in dirs]
        validSet = [(0, 1, 0, 0), (0, 1, 1, 1), (0, 1, -1, 1)]
    elif dir == 3:
        r -= 1
        dirs = [(c, r) for r, c in dirs]
        validSet = [(-1, 0, 0, 0), (-1, 0, -1, -1), (-1, 0, -1, 1)]
    else:
        r += 1
        dirs = [(-c, r) for r, c in dirs]
        validSet = [(1, 0, 0, 0), (1, 0, 1, 1), (1, 0, 1, -1)]

    stack = [(r, c, 5)]
    visited = [[False for _ in range(C)] for __ in range(R)]
    visited[r][c] = True

    board[r][c] = applied(board[r][c], 5)
    while stack:
        r, c, amt = stack.pop()
        amt -= 1
        if amt == 0:
            continue
        for dr, dc in dirs:
            notValid = False
            nr = r + dr
            nc = c + dc
            if oob(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            for vs in validSet:
                t, y, u, i = vs[0]+nr, vs[1]+nc, vs[2]+nr, vs[3]+nc
                if not valid(t, y, u, i):
                    notValid = True
                    break
            if notValid:
                continue
            stack.append((nr, nc, amt))
            board[nr][nc] = applied(board[nr][nc], amt)
            visited[nr][nc] = True


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
nwall = int(input())
walls = []
for _ in range(nwall):
    rr, cc, t = map(int, input().split())
    rr, cc = rr-1, cc-1
    if t == 0:
        walls.append([(rr-1, cc), (rr, cc)])
    else:
        walls.append([(rr, cc), (rr, cc+1)])

# preprocess board - (온도, 무슨 칸인지)
for r in range(R):
    for c in range(C):
        board[r][c] = (0, board[r][c])

# heater positions
heaters = []
for r in range(R):
    for c in range(C):
        if board[r][c][1] in (1, 2, 3, 4):
            heaters.append((r, c, board[r][c][1]))

chocolates = 0
while True:
    chocolates += 1
    # 1. 온풍기 바람 불기
    for r, c, dir in heaters:
        # blow(r, c, dir)  # se
        dfs(r, c, dir)
    # break
    # pnt(board)
    # 2. 온도 조절
    controlTemperature()  # se
    # 3. 바깥 온도 조절
    controlOutsideTemperature()
    cand = getCandidates()
    # 4. 조사
    if terminate(cand):
        print(walls)
        break


print("ans: ", chocolates)


# 7 8 1
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 2 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 2
# 2 4 0
# 2 3 1
# (3, 4) | (3, 5)

# 7 8 1
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 1
# 2 3 1
