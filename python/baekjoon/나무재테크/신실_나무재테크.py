'''
시작: 11:01
끝: 11:46
1. 봄 grow()
    - 어린 나무 순서대로 자신의 나이만큼 땅의 양분을 먹는다. 
    - 양분을 먹으면 나이가 1 증가한다.
    - 양분이 부족하면 양분을 먹지 못하고 즉시 죽는다.
2. 여름 decompose()
    - 죽은 나무가 자신의 나이//2 만큼의 양분으로 변한다.
3. 가을 reproduce()
    - 나이가 5의 배수인 나무에 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
4. 겨울 fertilize()
    - 로봇이 양분을 준다.
'''
from collections import defaultdict


N,M,K = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5 for _ in range(N)] for _ in range(N)]
tree_d = [[[] for _ in range(N)] for _ in range(N)]
def count_trees():
    global N
    cnt = 0
    for r in range(N):
        for c in range(N):
            cnt += len(tree_d[r][c])
    return cnt

def print_board(b):
    for r in b:
        s = ""
        for e in r:
            s = s + "\t"+str(e)
        print(s)
for _ in range(M):
    r, c, age = map(int,input().split())
    tree_d[r-1][c-1].append(age)

for r in range(N):
    for c in range(N):
        tree_d[r][c].sort()

def grow():
    '''
    - 어린 나무 순서대로 자신의 나이만큼 땅의 양분을 먹는다. 
    - 양분을 먹으면 나이가 1 증가한다.
    - 양분이 부족하면 양분을 먹지 못하고 즉시 죽는다.
    '''
    global dead_trees_l,N, tree_d, board
    for r in range(N):
        for c in range(N):
            new_tree_list = []
            for tree in tree_d[r][c]:
                if board[r][c]>=tree:
                    board[r][c]-=tree
                    new_tree_list.append(tree+1)
                else:
                    dead_trees_l.append([r,c,tree])
            tree_d[r][c]=new_tree_list

def decompose():
    '''
    - 죽은 나무가 자신의 나이//2 만큼의 양분으로 변한다.
    '''
    global dead_trees_l, board
    for r, c, age in dead_trees_l:
        board[r][c] += age//2

def reproduce():
    '''
    - 나이가 5의 배수인 나무에 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    '''
    global tree_d, N
    dr = [0,0,1,1,1,-1,-1,-1]
    dc = [1,-1,0,1,-1,0,1,-1]
    baby_trees = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for tree in tree_d[r][c]:
                if tree % 5 == 0 and tree > 0:
                    for d in range(8):
                        nr = r+ dr[d]
                        nc = c+ dc[d]
                        if 0<=nr<N and 0<=nc<N:
                            baby_trees[nr][nc] +=1
    for r in range(N):
        for c in range(N):
            tree_d[r][c] = [1 for _ in range(baby_trees[r][c])] + tree_d[r][c]

def fertilize():
    global board, A, N
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]

def solve():
    global K
    for _ in range(K):
        dead_trees_l = []
        grow()
        decompose()
        reproduce()
        fertilize()
    print(count_trees())

solve()