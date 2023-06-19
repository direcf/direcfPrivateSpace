#

def pnt():
    global board
    for row in board:
        print(row)
    print()


def move(r, c, dr, dc, repeat) -> tuple:
    global serial, cnt
    for _ in range(repeat):
        nr, nc = r+dr, c+dc
        # board[nr][nc] = cnt
        # cnt += 1
        serial.append(board[nr][nc])
        r, c = nr, nc
    return r, c


def spiral(board):
    global N, cnt, serial
    serial = []
    repeat = 1
    cnt = 1
    r, c = N//2, N//2
    while True:
        r, c = move(r, c, 0, -1, repeat)
        r, c = move(r, c, 1, 0, repeat)
        repeat += 1
        r, c = move(r, c, 0, 1, repeat)
        r, c = move(r, c, -1, 0, repeat)
        if (r, c) == (0, N-1):
            break
        repeat += 1
    for c in range(N-2, -1, -1):
        serial.append(board[r][c])
        # board[r][c] = cnt
        # cnt += 1
    return board, serial


def blast():
    for i in range(1, N*N):
        if serial[i] == 0:
            break
        j = i
        while j+1 < N*N and serial[i] == serial[j+1]:
            j += 1
        if j - i + 1 >= 4:
            for k in range(i, j+1):
                serial[j] = 0
        i = j


def throwIce(r, c, d, s):
    dr, dc = dirs[d]
    for i in range(s):
        r = r + dr
        c = c + dc
        if not (0 <= r < N and 0 <= c < N):
            continue
        board[r][c] = 0


def arange():
    pass


def split():
    pass


# board = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]
# N = len(board)
# r, c = N//2, N//2
# ↑, ↓, ←, → : 1 2 3 4
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ds = [tuple(map(int, input().split())) for _ in range(M)]
ds = [(d-1, s)for d, s in ds]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = (N//2, N//2)

pnt()
throwIce(r, c, ds[0][0], ds[0][1])
arange()
blast()
arange()
split()
