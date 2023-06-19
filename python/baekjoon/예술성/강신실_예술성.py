'''
start   
end     9:50
Step 1. 인접한 같은 숫자끼리 그룹을 만든다. => BFS
Step 2. 예술점수는 모든 그룹 쌍의 조화로움의 합으로 정의한다.
    그룹 a와 그룹 b의 조화로움은 (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수)*그룹 a를 이루고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값 * 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    그룹 쌍 간의 조화로움 값이 0보다 큰 조합인 조화로움값을 모두 더한 것을 초기 예술 점수라고 부른다.
    필요 정보: 그룹 칸 수, 맞닿은 변 수, 그룹을 이루고 있는 숫자
    그룹 칸 수: list
    맞닿은 변 수: dict 맞닿은 칸이 다른 그룹일 시 맞닿은 변 수에 1을 더해준다. 
    그룹을 이루고 있는 숫자: dict
'''
from collections import defaultdict
from collections import deque
import pdb
dr = [0,0,1,-1]
dc = [1,-1,0,0]
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
# pdb.set_trace()
def get_groups():
    global board
    groups = []
    def get_group(r, c, v):
        global dr, dc, board
        group = []
        q = deque()
        num = board[r][c]
        q.append([r, c])
        group.append([r,c])
        while q:
            cr, cc = q.popleft()
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0<=nr<n and 0<=nc<n and v[nr][nc]==False and board[nr][nc]==num:
                    v[nr][nc]=True
                    group.append([nr,nc])
                    q.append([nr,nc])
        return group
    v = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if v[r][c]==False:
                v[r][c]=True
                group = get_group(r, c, v)
                groups.append(group)
                print(len(group))
    return groups
    
def get_art_score(groups):
    global  dr, dc, n
    group_board = [[0 for _ in range(n)] for _ in range(n)]
    for i, group in enumerate(groups):
        for r, c in group:
            group_board[r][c]=i

    shared_edges = defaultdict(int)
    v = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0<=nr<n and 0<=nc<n and board[r][c] != board[nr][nc] and v[r][c][d]==False:
                    a = min(group_board[r][c], group_board[nr][nc])
                    b = max(group_board[r][c], group_board[nr][nc])
                    shared_edges[(a,b)] +=1
                    v[r][c][d]=True

    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수)
    # *그룹 a를 이루고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값 * 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    t_score = 0
    for k, v in shared_edges.items():
        a, b= list(k)
        ar, ac = groups[a][0]
        br, bc = groups[b][0]
        na = board[ar][ac]
        nb = board[br][bc]

        s = (len(groups[a]) + len(groups[b]))*na*nb*(v//2)
        print(k, s)
        t_score += s
    return t_score

'''
배열 회전시키기.
cos x   -sinx
sinx    cosx

시계 90도 = -90도   x = y, y = -x
n_board[c][n-r-1] = board[r][c]
0   1
-1  0

반시계 90도         x =-y, y = x
0   -1
1   0
'''
def print_board(b):
    for l in b:
        s = ''
        for e in l:
            s = s + str(e) + '\t'
        print(s)
def rotate_cross(center):
    # 반시계방향
    global n, board
    n_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        r = center
        c = i
        n_board[n-c-1][r] = board[r][c]
        c = center
        r = i
        n_board[n-c-1][r] = board[r][c]
    # print_board(n_board)
    for i in range(n):
        r = center
        c = i
        board[r][c] = n_board[r][c]
        c = center
        r = i
        board[r][c] = n_board[r][c]
    return n_board
def rotate_square(start, length):
    global board
    rr = start[0]
    cc = start[1]
    print("STR", start)
    n_board = [[0 for _ in range(n)] for _ in range(n)]
    '''if start == [3,3]:
        pdb.set_trace()'''
    for r in range(rr, rr+length):
        for c in range(cc, cc+length):
            # pdb.set_trace()
            n_board[c][length-r-1] = board[r][c]
            
    for r in range(rr, rr+length):
        for c in range(cc, cc+length):
            board[r][c] = n_board[r][c]
    print("HERE")
    print_board(n_board)
def rotate():
    global board
    center = n//2
    n_board = rotate_cross(center)
    for rr, cc in [[0,0],[0,1],[1,0],[1,1]]:
        r = rr*(center+1)
        c = cc *(center+1)
        rotate_square([r,c], center)
    
    





def solve():
    ans = 0
    for _ in range(1):
        groups = get_groups()
        score = get_art_score(groups)
        ans += score
        rotate()
    print(ans)

solve()