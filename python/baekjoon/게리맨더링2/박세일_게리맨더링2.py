# 개리멘ㄷ링2
# 6:14 ~

# 연결되어있지 않는 경우가 있을까?
# 중간에 통하는 인접한 구역은 0개 이상이어야 하고,
# 모두 같은 선거구에 포함된 구역이어야 한다.

# (x,y)도 랜덤, d1,d2도 랜덤.
# 대신 d1,d2의 범위는 정해짐.

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ans = 1000000000

def find_d(x):
    d_sum = n - 1 - x
    arr = []
    if d_sum < 2:
        return arr
    for d1 in range(1, d_sum):
        d2 = d_sum - d1
        arr.append([d1,d2])

def part(y,x,d1,d2):
    global n
    # 1,2,3,4 선거구 합 구하기.
    first = 0
    for i in range(y):
        for j in range(x+d1-i):
            first += board[i][j]

    second = 0
    for i in range(y-d1+d2-1):
        for j in range(n-(x+d1)+1, n):
            second += board[i][j]
    if n - (x + d1 + d2) > 0:
        # 추가로 더 더해준다.
        for i in range(n-(x+d1)+2, n):


    third = 0
    for i in range(y):
        for j in range(x + d1 - i):
            third += board[i][j]

    fourth = 0
    for i in range(y):
        for j in range(x + d1 - i):
            fourth += board[i][j]


for y in range(1, n-1):
    for x in range(n-2):
        # x 범위에 해당되는 모든 d1, d2를 구한다. d1,d2는 1보다 크다.
        d_list = find_d(x)
        for d in d_list:
            part(y,x,d[0],d[1])
        # 각 구역의 총합 정리하고, min,max 값 차이가 ans보다 작으면 변경.


