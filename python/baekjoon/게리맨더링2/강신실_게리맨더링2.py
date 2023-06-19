'''
시작:   6:14
끝:     7:45
선거구를 5개로 나눈다.
모든 R, C, d1, d2에 대해 선거구를 나누고, 시도해 봐야한다.=> dfs
d1, d2>=1, 0<R<R+d1+d2<N, 0<=C-d1<C<C+d2<N

1) 한 선거구에 포함되어 있느 구역은 모두 연결되어있어야 한다.
2) 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.
1. 기준점 (x,y)와 경계의 길이 d1, d2를 정한다.
2. 경계선을 정한다.
3. 경계선과 경계선의 안에 포함되어 잇는 곳은 5번 선거구이다.
4. 5번 선거구에 포함되지 않은 구역 (r,c)의 선거구 번호는 다음 기준을 따른다.
x = R, y = C
1번 선거구: 0<=r<R+d1-1, 0<=c<=C-1
2번 선거구: 0<=r<R+d2-1, C-1<c<N
3번 선거구: R+d1-1<=r<N, 0<=c<C-d1+d2-1
4번 선거구: R+d2-1<r<N, C-d1+d2-1<=c<N
선거구를 나누는 방법 중에서 인구가 가장ㅇ 많은 선거구와 가장 적은 선거구 인구 차이의 최솟값?
1. 선 긋기
2. 5번 구 구하기
3. 나머지 선거구 나누기
5. 각 구 인구수 구하기
6. 최솟값 구하기
'''
from collections import defaultdict, deque
import pdb

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
minn = 1e9
def print_board(b):
    for l in b:
        s = ""
        for e in l:
            s = s + str(e)+"\t"
        print(s)
def split_group(l):
    global n, board
    g_board = [[0 for _ in range(n)]for _ in range(n)]
    d1, d2, R, C = l
    groups = defaultdict(list)
    point_l = [[R+d1, C-d1],[R+d1+d2,C-d1+d2],[R+d2, C+d2],[R,C]]
    dr = [1,1,-1,-1]
    dc = [-1,1,1,-1]

    sr, sc = R, C
    for d, ep in enumerate(point_l):
        er, ec = ep
        q = deque()
        q.append([sr, sc])
        g_board[sr][sc]=5
        while q:
            cr, cc = q.popleft()
            if cr == er and cc == ec:
                sr = er
                sc = ec
                break
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<=nr<n and 0<=nc<n and g_board[nr][nc]==0:
                g_board[nr][nc]=5
                q.append([nr,nc])
    '''
    x = R, y = C
    1번 선거구: 0<=r<R+d1-1, 0<=c<=C-1
    2번 선거구: 0<=r<R+d2-1, C-1<c<N
    3번 선거구: R+d1-1<=r<N, 0<=c<C-d1+d2-1
    4번 선거구: R+d2-1<r<N, C-d1+d2-1<=c<N
    '''
    # 1번 선거구
    # print("1번")
    # print(R+d1-1, C-1)
    for r in range(0, R+d1):
        for c in range(0, C+1):
            if g_board[r][c]==0:
                g_board[r][c]=1
            else:
                break
    # 2번 선거구
    # print("2번")
    # print(C, n, 0, R+d2)
    for c in range(C, n):
        for r in range(0, R+d2+1):
            if g_board[r][c]==0:
                g_board[r][c]=2
            else:
                break
    # 3번 선거구
    # print("3번")
    # print(R+d1, n, 0, C-d1+d2)
    for r in range(R+d1, n):
        
        for c in range(0, C-d1+d2):
            if g_board[r][c]==0:
                g_board[r][c]=3
            else:
                break
    # 4번 선거구
    # print("4번")
    # print(n-1, R+d2+1, C-d1+d2-1, n)
    for r in range(n-1, R+d2, -1):
        for c in range(n-1, C-d1+d2-1, -1):
            # print("r,c", r,c)
            if g_board[r][c]==0:
                g_board[r][c]=4
            else:
                break
    for r in range(n):
        for c in range(n):
            g_name = g_board[r][c]
            if g_name==0:
                g_board[r][c]=5
    return g_board
def get_populations(b):
    global board, n
    populations = [0 for _ in range(6)]
    for r in range(n):
        for c in range(n):
            g_name = b[r][c]
            populations[g_name] += board[r][c]
    return populations[1:]

            



def dfs(cnt, candi):
    global minn, n
    if cnt == 4:
        # print("here")
        groups_board = split_group(candi)
        # pdb.set_trace()
        populations_groups = get_populations(groups_board)
        dif = max(populations_groups)-min(populations_groups)
        if dif<minn:
            # print("here")
            # print_board(groups_board)
            # print("minn", dif)
            minn = dif
        return
    else:
        '''
        d1, d2>=1, 0<R<R+d1+d2<N, 0<=C-d1<C<C+d2<N
        '''
        
        if cnt <= 1:
            for d in range(1, n):
                dfs(cnt+1, candi+[d])
        elif cnt == 2:
            d1, d2 = candi
            for r in range(n-d1-d2):
                dfs(cnt+1, candi+[r])
        else:
            d1, d2, r = candi
            for c in range(d1,n-d2):
                dfs(cnt+1, candi+[c])
def solve():
    
    dfs(0, [])
    print(minn)
solve()