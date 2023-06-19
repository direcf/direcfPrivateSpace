from collections import defaultdict
N, M, H, K = map(int, input().split()) # N 격자크기(홀수), M 도망자 수, H, 나무 수, K 시도횟수
tmp_runner = []
tmp_tree = []
# dx, dy = ((0,0), (1,-1)), ((1,-1), (0,0)) # 좌/우 // 아래/위
dx, dy = (0,1,0,-1), (1,0,-1,0) # 좌 / 아래 / 우 / 위
dx2, dy2 = ((-1,0,1,0),(1,0,-1,0)), ((0,1,0,-1),(0,1,0,-1)) # (위,오른쪽,아래,왼쪽) / (아래,오른쪽,위,왼쪽)
# (중요!!) 여기서 defaultdict을 쓰는게 좋을까 아니면 그냥 list를 쓰는게 좋을까? >> 가능하면 defaultdict과 queue를 애용하자!
# (idea1) 거리를 3재는건 bfs로 dismap을 만들어서 푸는게 아닌 그냥 manhattan distance 구해서 풀면 된다
runner = defaultdict(list)
tree = []
for _ in range(M):
    tmp_runner = list(map(int, input().split()))
    if tmp_runner[2] == 1:
        tmp_dir = 0
    elif tmp_runner[2] == 2:
        tmp_dir = 1
    runner[(tmp_runner[0]-1, tmp_runner[1]-1)].append(tmp_dir)

for _ in range(H):
    tmp_tree = list(map(int,input().split()))
    tree.append([tmp_tree[0]-1, tmp_tree[1]-1])

def move_runner():
    global runner, x, y
    tmp_runner = defaultdict(list)
    for k, v_zip in runner.items():
        if abs(x-k[0]) + abs(y-k[1]) <= 3:
            for v in v_zip: # v (int)
                nx, ny = k[0]+dx[v], k[1]+dy[v]

                if 0<=nx<N and 0<=ny<N:
                    if nx == x and ny == y:  # 술래가 있는 곳으로는 가지않는다 (가만히 있는다)
                        tmp_runner[(k[0], k[1])].append(v)
                        continue
                    tmp_runner[(nx,ny)].append(v)
                else:
                    v = (v + 2) % 4 # 방향바꾸기
                    nx, ny = k[0]+dx[v], k[1]+dy[v]
                    if nx == x and ny == y:  # 술래가 있는 곳으로는 가지않는다 (가만히 있는다)
                        tmp_runner[(k[0], k[1])].append(v)
                        continue
                    tmp_runner[(nx, ny)].append(v)
        else:
            tmp_runner[k].extend(v_zip)
            continue
    runner = tmp_runner

#### 1 1 2 2로 푸는것보다 dfs로 푸는것이 더 일반적일 것 같다 >> (하지만 computation과 관련된 고민은 필요하다)
def move_man():
    global x, y, dir, route, visited
    if route == 0:
        nx, ny = x + dx2[route][dir], y + dy2[route][dir]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            x, y = nx, ny
            visited[x][y] = True
            dir  = (dir + 1) % 4 #### (중요!!!) 아래 코드와 방식이 다르다!!

            nx, ny = x + dx2[route][dir], y + dy2[route][dir]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                pass
            else:
                dir = (dir - 1) % 4 #### (중요!)

        if x == 0 and y == 0:
            dir = 0
            route = 1
            visited = [[True] * N for _ in range(N)]
            visited[x][y] = False

    elif route == 1:
        nx, ny = x + dx2[route][dir], y + dy2[route][dir]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == True: # 갈수없는곳이어야 회전한다
            x, y = nx, ny
            visited[x][y] = False

            # (중요!!!!!) 방향정하기 (갈 수 없을때 방향을 바꿔준다 + nx, ny를 두 번 사용해야한다)
            nx, ny = x + dx2[route][dir], y + dy2[route][dir]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == True: # 갈 수 있는 곳이다
                pass
            else:
                dir = (dir + 1) % 4

        if x == N//2 and y == N//2:
            dir = 0
            route = 0
            visited = [[False] * N for _ in range(N)]
            visited[x][y] = True

def catch_runner():
    global runner, x, y, dir, route, del_tmp
    # 현재 나무아닌곳에서 잡은지 확인 후 잡기
    del_tmp = []
    if (x,y) in runner.keys():
        if [x,y] not in tree:
            del_tmp.append([x,y])

    # 3개의 추가 포지션 구하기
    search_pos = []
    for i in range(1,4):
        search_pos.append([x+dx2[route][dir] * i, y+dy2[route][dir] * i])


    for k in runner.keys():
        if list(k) not in tree:
            if list(k) in search_pos:
                del_tmp.append(list(k))



def solve():
    global runner, tree, x, y, dir, route, visited
    score = 0
    x,y = N//2, N//2
    dir = 0
    route = 0
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    for step in range(K):
        print("STEP",step+1)
        move_runner()
        print("RUNNER" , runner)
        move_man()
        print("MAN", x,y,route,dir)
        catch_runner()
        print("CAUGHT MAN", del_tmp)

        for ele in del_tmp:
            # print(runner[tuple(ele)])
            score += (step + 1) * len(runner[tuple(ele)])
            del runner[tuple(ele)]
    print(score)
solve()

