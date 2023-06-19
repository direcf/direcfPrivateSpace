# 핵심: 2개의 팀(스타트팀, 링크팀)으로 나눠야 한다. 이때, combination을 사용하면 좋지 않을까 생각된다.
# 시간: 30분
import sys
sys.stdin = open('number3.txt', 'r')

# step1. input값 받아오
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# step2. combination을 구현해서 팀 나누기
def comb(mat, k):
    team1 = []
    n = len(mat)
    if k == 1:
        for i in range(n):
            team1.append([mat[i]])
    elif k > 1:
        for i in range(n):  # 0,1,2,3,4,5 // k = 2
            for j in comb(mat[i+1:], k-1):
                team1.append([mat[i]] + j)
    return team1

people = [i for i in range(N)] # [0,1,2,3,4,5]
team1 = comb(people, len(people) // 2)
# print(team1) #  [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 1, 5], [0, 2, 3], [0, 2, 4], [0, 2, 5], [0, 3, 4], [0, 3, 5], [0, 4, 5], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
# print(team2) # [[3, 4, 5], [2, 4, 5], [2, 3, 5], [2, 3, 4], [1, 4, 5], [1, 3, 5], [1, 3, 4], [1, 2, 5], [1, 2, 4], [1, 2, 3], [0, 4, 5], [0, 3, 5], [0, 3, 4], [0, 2, 5], [0, 2, 4], [0, 2, 3], [0, 1, 5], [0, 1, 4], [0, 1, 3], [0, 1, 2]]

# step3. 점수매기기
team1_score = []
for team in team1:
    score = 0
    for i in team:
        for j in team:
            if i!=j:
                score += board[i][j]
    team1_score.append(score)
# print(team1_score) # [9, 11, 13, 15, 13, 15, 17, 17, 19, 21, 15, 17, 19, 19, 21, 23, 21, 23, 25, 27]

# step4. 대칭성 이용해서 최소가 되는 시너지값 구하기
answer = []
for index in range(len(team1_score)):
    answer.append(abs(team1_score[index] - team1_score[len(team1_score)-1-index]))
print(min(answer))