'''
뱀이 벽 혹은 자신과 부딛히면 게임이 끝난다.

'''
n = int(input())
k = int(input())
apples = []
for _ in range(k):
    r, c = map(int,input().split())
    apples.append([r,c])
    