'''
스타트 팀과 링크 팀의 능력치 차이의 최소값을 구한다.
combination을 모두 구하기.
1) dfs로 선택하기.
'''
from sys import stdin
n = int(stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int,stdin.readline().split())))

minn = int(1e9)
v = [False for _ in range(n+1)]
visited = []
def get_diff_score(l):
    global board, visited
    a = 0
    b = 0
    all_list = list(range(n))
    a_l = l
    b_l = list(set(all_list)-set(l))
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            a += board[a_l[i]][a_l[j]]
            b += board[b_l[i]][b_l[j]]
    return abs(a-b)

def dfs(cnt, candi,idx):
    global n, board, minn
    if cnt == n//2:
        score_c = get_diff_score(candi)
        if score_c<minn:
            # print(candi)
            minn = score_c
        if minn == 0:
            print(0)
            exit(0)
        return
    else:
        for i in range(idx, n):
            if v[i]==False:
                v[i]=True
                dfs(cnt+1, candi+[i],i+1)
                v[i]=False
for ii in range(n):
    dfs(1, [ii],ii+1)


print(minn)

