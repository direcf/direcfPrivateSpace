'''
start 10:10
T: 상담을 완료하는데 걸리는 기간
P: 상담을 했을 때 받을 수 있는 금액
N+1때 퇴사
할 수 있는 액션: 상담을 맡는다 vs 맡지 않는다.
모든 경우의 수에 대해서 구하기=> 2^15: 2^10*2^5=35ms
'''
import pdb
import copy

n = int(input())
p = []
t = []
s = [False for _ in range(n)]
sl = []
ans = 0
for _ in range(n):
    tt, pp = map(int,input().split())
    p.append(pp)
    t.append(tt)

def book_schedule(start_day, duration):
    global s
    for i in range(start_day, start_day+duration):
        s[i]=True


def dfs(cnt, candi, cl):
    global s, ans, p, t,n
    # pdb.set_trace()
    if cnt == n:
        if candi>ans:
            # print("CL",cl)
            # print(candi)
            ans = candi
            return
    else:
        for i in [True, False]:
            if i == True and s[cnt]==False and cnt+t[cnt]<=n:
                # print("CL",cl)
                backup= copy.deepcopy(s)
                book_schedule(cnt, t[cnt])
                dfs(cnt+1, candi+p[cnt], cl+[cnt])
                s = backup
            else:
                dfs(cnt+1, candi,cl)


dfs(0,0,[])
print(ans)