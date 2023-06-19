import sys
sys.stdin = open('number13.txt','r')
# 시간: 20시40분~21시50분
from collections import deque
N = int(input()) # 3 ≤ n ≤ 29
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# step1. 칸 나누기(숫자가 다른걸로, bfs)
# step2. 인접해있는 블럭의 갯수 구하기
# step3. 초기예술 점수 구하기
# 그때그때 바로 구할 수 있나? 예술점수를? 없다 어딘가 저장해둬야 한다

dx, dy = (1,0,-1,0), (0,1,0,-1)
def group_numbering(mat):
    visited = [[False] * N for _ in range(N)]
    new_mat = [[0] * N for _ in range(N)] # group으로 나누기

    group_num = -1
    # (중요) group 구분
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:

                group_num += 1
                number = mat[i][j]
                new_mat[i][j] = group_num # (중요) 이거 찾지못해서 20분 소요
                # print(mat, i, j ,number)
                # print(new_mat)
                q = deque()
                q.append((i,j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]

                        if 0<=nx<N and 0<=ny<N:
                            # print(nx,ny,number, group_num)
                            if visited[nx][ny] == False and mat[nx][ny] == number:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                new_mat[nx][ny] = group_num
    # print(visited)
    return new_mat, group_num

# print(group_numbering(board)) # [[0, 1, 1, 2, 2], [1, 1, 1, 2, 2], [1, 1, 3, 2, 3], [1, 1, 3, 3, 3], [1, 1, 3, 3, 3]]

def art_score(mat, new_mat, group_num):
    correlation = [[0] * group_num for _ in range(group_num)]
    group_block_num = [0] * group_num # [0,0,0,0]
    visited = [[False] * N for _ in range(N)]
    result = [0] * group_num

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                number = mat[i][j]
                group_block_num[new_mat[i][j]] = mat[i][j]
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]

                        if 0<=nx<N and 0<=ny<N:
                            if visited[nx][ny] == False and mat[nx][ny] == number:
                                visited[nx][ny] = True
                                q.append((nx,ny))
                                cnt += 1
                            elif visited[nx][ny] == False and mat[nx][ny] != number:
                                max_val = max(new_mat[nx][ny], new_mat[i][j])
                                min_val = min(new_mat[nx][ny], new_mat[i][j])
                                correlation[min_val][max_val] += 1
                                # group_block_num[new_mat[i][j]] += 1
                result[new_mat[i][j]] = cnt
    # print(result) # [1, 11, 5, 8]
    # print(group_block_num) # [2, 6, 4, 0]
    # print(correlation) # [[0, 2, 0, 0, 0], [0, 0, 2, 4, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # score 계산
    score = 0
    for i in range(group_num):
        for j in range(i+1,group_num):
            score += (result[i] + result[j]) * group_block_num[i] * group_block_num[j] * correlation[i][j]

    return score





# step1. 십자모양은 반시계방향 회전
# step2. 십자이외의 부분 4개는 모두 시계방향 회전

# step_last. 초기 + 1회전 + 2회전 + 3회전 예술점수의 합 계산


# import copy
def solve():
    global board
    total_score = 0
    # 초기값 세팅
    new_board, group_num = group_numbering(board)
    total_score += art_score(board, new_board, group_num + 1)
    # rot_board = copy.deepcopy(board)
    # 회전 + scoring 3회
    for _ in range(3):
        # N은 반드시 홀수입니다
        my_board = [[0] * N for _ in range(N)]
        # (step1) 중앙선들 반시계 회전
        # 세로줄 update
        for i in range(N):
            my_board[i][N//2] = list(zip(*board))[::-1][i][N//2]
        # 가로줄 update
        for j in range(N):
            my_board[N//2][j] = list(zip(*board))[::-1][N//2][j]

        # (step2) 중앙선 제외 부분 시계회전
        # print(board)
        # print(board[0:3][0:3]) # [[1, 2, 2, 3, 3], [2, 2, 2, 3, 3], [2, 2, 1, 3, 1]]
        # print(board[0:N//2][0:N//2]) # [[1, 2, 2, 3, 3], [2, 2, 2, 3, 3]]

        for sx in range(0,N,N//2+1):
            for sy in range(0,N,N//2+1):
                for i in range(N//2):
                    for j in range(N//2):
                        my_board[sx+j][sy+N//2-i-1] = board[sx+i][sy+j]

        board = my_board
        # print(board)
        new_board, group_num = group_numbering(board)
        # print(new_board)
        total_score += art_score(board, new_board, group_num + 1)
        # print()

    print(total_score)


solve()