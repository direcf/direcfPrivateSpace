# 술래잡기
#도망자는 좌우, 상하 두 유형
# 오른쪽, 아래쪽 보고 시작.
# 도망자 -> 술래 -> 도망자 -> 술래
# 거리 3 이하인 사람만 움직인다. abs(x1-x2) + abs(y1-y2)
# 문제 함수 구현까지 1시간20분
# 총 시간 2시간 52분. -> 특히 술래 움직이기가 어려웠다.

# 격자크기, 도망자수, 나무수, 술래이동수
n,m,h,k = map(int, input().split())
runner = [] # [y,x,2], [y,x,3]
trees = []
score = 0
mp = [n//2, n//2]
ans = 0
for _ in range(m):
    zx = list(map(int, input().split()))
    if zx[2] == 1:
        # 좌우 우 먼저
        runner.append([zx[0]-1, zx[1]-1, 3])
    else:
        # 상하 하 먼저
        runner.append([zx[0]-1, zx[1]-1, 1])

for _ in range(h):
    zxx = list(map(int, input().split()))
    trees.append([zxx[0]-1, zxx[1]-1])

# 상 하 좌 우
dy = [-1, +1, +0, +0]
dx = [+0, +0, -1, +1]

def change_dir(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    else:
        return 2


def escape():
    global runner
    new_runner = []
    for i in range(len(runner)):
        if abs(mp[0]-runner[i][0]) + abs(mp[1]-runner[i][1]) <= 3:
            # 바라보는방향 1칸
            ny = runner[i][0] + dy[runner[i][2]]
            nx = runner[i][1] + dx[runner[i][2]]
            if ny>=0 and nx>=0 and ny<n and nx<n:
                # if mp[0] != ny or mp[1] != nx:
                if mp[0] == ny and mp[1] == nx:
                    # 있다면 대기.
                    new_runner.append(runner[i])

                else:
                    # 술래가 없다면 원래 방향으로 이동
                    new_runner.append([ny, nx, runner[i][2]])

            else:
                # 방향 틀기.
                dir2 = change_dir(runner[i][2])
                ny = runner[i][0] + dy[dir2]
                nx = runner[i][1] + dx[dir2]
                if mp[0] == ny and mp[1] == nx:
                    # 있다면 대기.
                    new_runner.append(runner[i])
                else:
                    # 술래없다면 반대 방향으로 이동
                    new_runner.append([ny, nx, dir2])
        else:
            new_runner.append(runner[i])



    runner = new_runner


# 술래이동method
# cnt가 있고.
# cnt가 n-1면 반대로.
# 무조건 순서는 상우하좌
# dcnt = 2
# main = 1부터 시작
# d = 1부터 시작. d가 0되면 dcnt-1하고.
# dcnt가 만약 0이면 dcnt = 2로 변경. main도 2로 변경
# dir = 0(상부터 시작)
dcheck = 2
main = 1
remain = 1
dir = 0
cnt = 0
reverse = False
# 상 우 하 좌
dy2 = [-1, +0, +1, +0]
dx2 = [+0, +1, +0, -1]
def mp_move():


    global dcheck
    global main
    global remain
    global dir
    global cnt
    global reverse

    # 술래 이동
    mp[0] += dy2[dir]
    mp[1] += dx2[dir]


    remain += -1
    cnt += 1

    if remain == 0:
        # 방향 전환 + remain 갱신
        dcheck += -1
        if dcheck == 1:
            remain = main
        else:
            if reverse:
                main += -1
            else:
                main += 1
            remain = main
            dcheck = 2
        if reverse:
            dir = (dir-1) % 4
        else:
            dir = (dir + 1) % 4

    if cnt == n**2 - 1:
        # 끝지점 도달하면
        if reverse:
            # 중앙으로 가는 방향이면
            # 방향 뒤집어 + reverse
            dir = 0 # 방향 상으로 변경
            reverse = False
            # 재설정
            dcheck = 2
            main = 1
            remain = 1
            cnt = 0
        else:
            # (0,0)으로 가는 방향이면
            # 방향 뒤집어 + reverse
            dir = 2 # 방향 하로 변경
            reverse = True
            # 재설정
            dcheck = 1
            main = n # 여기서 많이 헤맸다.
            remain = n - 1
            cnt = 0


def catch(nscore):
    global dir
    global ans
    global runner

    i = 0
    new_runner2 = []
    # 잡으면 러너 삭제해야함.
    catch_cnt = 0
    del_runner_idx = []
    while i < 3:
        ny = mp[0] + dy2[dir] * i
        nx = mp[1] + dx2[dir] * i
        if ny>=0 and nx>=0 and ny<n and nx<n:
            if [ny,nx] not in trees:
                for ridx in range(len(runner)):
                    if runner[ridx][0] == ny and runner[ridx][1] == nx:
                        # 2명일수 있다.
                        catch_cnt += 1
                        del_runner_idx.append(ridx)
        else:
            break
        i+=1

    # 새로운 러너배열로 저장 delete 제외하고
    new_runner3 = []
    for i in range(len(runner)):
        if i not in del_runner_idx:
            new_runner3.append(runner[i])
    runner = new_runner3
    ans += (nscore * catch_cnt)


for i in range(k):
    # if not runner:
    #     break
    escape()
    mp_move()
    catch(i+1)

print(ans)
