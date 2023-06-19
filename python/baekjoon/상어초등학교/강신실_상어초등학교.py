'''
start   6:40
end     7:36
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


최대 자리 수: 400
400*20 = 8000
완전 탐색으로 해결 가능.
1. 좋아하는 학생 수
2. 인접한 빈칸 수
3. - r
4. - c

순서대로 많은 순으로 정한다. 
'''
import pdb
import math
from collections import defaultdict
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
d = {}
loc = defaultdict(list)
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def print_board(b):
    for l in b:
        s = ''
        for e in l:
            s = s + str(e) + '\t'
        print(s)
def get_score():
    global board, d, loc, n, dr, dc
    score = 0
    for k, l in d.items():
        r, c = loc[k]
        cnt = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<n and 0<=nc<n and board[nr][nc] in l:
                cnt +=1
        if cnt>0:
            score += (math.pow(10, cnt-1))
    return score

def get_location(student_list):
    global board, n, d, dr, dc
    '''
    1. 좋아하는 학생 수 :  모든 칸 찾기
    2. 인접한 빈칸 수 : 
    3. - r
    4. - c
    '''
    s = student_list[0]
    likes = student_list[1:]
    l = []
    
    for r in range(n):
        for c in range(n):
            cnt_likes = 0
            cnt_blanks = 0
            if board[r][c]==0:
                for dd in range(4):
                    nr = r + dr[dd]
                    nc = c + dc[dd]
                    if 0<=nr<n and 0<=nc<n :
                        if board[nr][nc] in likes:
                            cnt_likes += 1
                        elif board[nr][nc]==0:
                            cnt_blanks += 1
                l.append([cnt_likes, cnt_blanks, r, c])
    l = sorted(l, key = lambda x : [-x[0], -x[1], x[2], x[3]])
    idx =0
    # if s == 9:
    #     pdb.set_trace()
    # pdb.set_trace()
    for e in l:
        r, c = e[2:]
        if board[r][c] > 0:
            idx +=1
        else:
            break
    return l[idx][2:]



for i in range(n*n):
    student_list = list(map(int,input().split()))
    d[student_list[0]] = student_list[1:]
    r, c = get_location(student_list)
    # pdb.set_trace()
    loc[student_list[0]] = [r,c]
    board[r][c] = student_list[0]
# print_board(board)
print(int(get_score()))  
