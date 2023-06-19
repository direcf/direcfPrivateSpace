'''
n개의 수로 이루어진 수열이 주어진다. 수와 수 사이에 끼워넣을 수 있는 n-1개의 연산자가 주어진다.
연산자는 4개로 이루어져있다.
식의 계산은 우선순위 무시하고 앞에서부터 진행한다.
나눗셈은 몫만 취한다.
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼다.
n개의 수와 n-1개의 연산자가 주어졌을 대 만들 수 있는 식의 결과가 최대인 것과 최소인 것은?

연산자의 개수를 입력으로 받았을 경우, 조합을 어떤식으로 모두 구할 것인가
dfs로 모든 경우의 수를 수행한다.
'''
n = int(input())
numbers = list(map(int,input().split()))
op = list(map(int,input().split()))
minn = int(1e9)
maxx = -int(1e9)
def dfs(cnt, candi,cl):
    global n, numbers, op, minn, maxx
    if cnt == n:
        if candi>maxx:
            maxx = candi
            # print(cl, candi)
        if candi<minn :
            minn = candi
            # print(cl, candi)
        return
    for i in range(4):
        if op[i]>0:
            op[i]-=1
            if i == 0:
                # 덧셈
                n_candi = candi+numbers[cnt]
            elif i == 1:
                # 뺄셈
                n_candi = candi-numbers[cnt]
            elif i == 2:
                # 곱셈
                n_candi = candi*numbers[cnt]
            elif i == 3:
                # 나눗셈
                if candi<0:
                    n_candi = -((-candi)//numbers[cnt])
                else:
                    n_candi = candi//numbers[cnt]
            dfs(cnt+1, n_candi,cl+[i])
            op[i]+=1

dfs(1,numbers[0],[])
print(maxx)
print(minn)