# 방향 d
# 거리 s
# 6:20-
dx = [1,2,3,4] # 상 하 좌 우
direct = {1:"up", 2:"down",3:"left",4:"right"}
# 1. 블리자드 스킬: 삭제 -> 이동 -> (4개 이상 시 폭파(삭제) -> 이동) 이걸 반복
# 2. 구슬 변화: 구슬그룹을 개수, 구슬숫자로 변경
# 상하좌우가 현재 끝에 있는 상황의 값이 몇인지 알아야함.

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(m):
    d, s = map(int, input().split())

    if direct[d] == "up":
        for i in range(1,s+1):
            arr[(n - 1)//2 - i][(n - 1) // 2] = 0
    elif direct[d] == "down":
        for i in range(1,s+1):
            arr[(n - 1)//2 + i][(n - 1) // 2] = 0
    elif direct[d] == "left":
        for i in range(1,s+1):
            arr[(n-1)//2][(n-1)//2 - i] = 0
    elif direct[d] == "right":
        for i in range(1,s+1):
            arr[(n-1)//2][(n-1)//2 + i] = 0

    for v in arr:
        print(v)

    # 땡기는 작업.
    # 돌면서 땡기면서 만약 0이면 그 다음 값을 땡겨온다.
    # 좌 하 우 상 순으로 2개씩 올라간다.
    # 0이 2번 연속으로 나오거나, 모든 칸 다 돌았을 때 탈출
    cnt = 1
    i = 0
    exit = True
    zero_flag = False
    col_idx = (n-1)//2
    row_idx = (n-1)//2
    new_arr = []
    cur_group = -1
    cur_count = 0
    ans_dict = {1:0,2:0,3:0}
    def add_bomb(col_idx, row_idx):
        global cur_count
        global cur_group
        global bomb_flag
        if cur_group == -1:
            cur_count = 1
            cur_group = arr[col_idx][row_idx]
        else:
            if arr[col_idx][row_idx] == cur_group:
                cur_count += 1
            else:
                if cur_count >= 4:
                    # 4개 연속의 경우면
                    ans_dict[cur_group] = ans_dict[cur_group] + cur_count
                    cur_group = new_arr.pop()
                    cur_count = new_arr.pop()
                if arr[col_idx][row_idx] == cur_group:
                    # while 문 돌기.
                    cur_count += 1
                else:
                # 기존의 cur_group 더해주고 새롭게 변경
                    new_arr.append(cur_count)
                    new_arr.append(cur_group)
                    cur_count = 1
                    cur_group = arr[col_idx][row_idx]
        return

    # 블리자드
    while exit and cnt < n*n:
        # 좌 하
        i += 1
        for j in range(2):
            if not exit:
                break
            if j % 2 == 0:
                for _ in range(i):
                    print("left")
                    row_idx += -1
                    if arr[col_idx][row_idx] == 0:
                        # 0이 연속인 경우
                        if zero_flag == True:
                            exit = False
                            break
                        else:
                            zero_flag = True
                    else:
                        zero_flag = False
                        add_bomb(col_idx, row_idx)
                    cnt += 1
                    if cnt >= n*n:
                        exit = False
                        break
            else:
                for _ in range(i):
                    print("down")
                    col_idx += +1
                    if arr[col_idx][row_idx] == 0:
                        if zero_flag == True:
                            exit = False
                            break
                        else:
                            zero_flag = True
                    else:
                        zero_flag = False
                        add_bomb(col_idx, row_idx)
                    cnt += 1
                    if cnt >= n * n:
                        exit = False
                        break

        if not exit:
            break

        # 우 위
        i += 1
        for j in range(2):
            if not exit:
                break
            if j % 2 == 0:
                for _ in range(i):
                    print("right")
                    row_idx += +1
                    if arr[col_idx][row_idx] == 0:
                        if zero_flag == True:
                            exit = False
                            break
                        else:
                            zero_flag = True
                    else:
                        zero_flag = False
                        add_bomb(col_idx, row_idx)
                    cnt += 1
                    if cnt >= n * n:
                        exit = False
                        break
            else:
                for _ in range(i):
                    print("up")
                    col_idx += -1
                    if arr[col_idx][row_idx] == 0:
                        if zero_flag == True:
                            exit = False
                            break
                        else:
                            zero_flag = True
                    else:
                        zero_flag = False
                        add_bomb(col_idx, row_idx)
                    cnt += 1
                    if cnt >= n * n:
                        exit = False
                        break

    ### new_arr를 다시 넣어준다.
    i = 0
    col_idx = (n - 1) // 2
    row_idx = (n - 1) // 2
    new_arr_idx = 0
    exit = True
    while exit:
        # 좌 하
        i += 1
        for j in range(2):
            if exit == False:
                break
            if j == 0:
                for _ in range(i):
                    row_idx += -1
                    arr[col_idx][row_idx] = new_arr[new_arr_idx]
                    new_arr_idx += 1
                    if new_arr_idx >= len(new_arr):
                        exit = False
                        break
            else:
                for _ in range(i):
                    col_idx += +1
                    arr[col_idx][row_idx] = new_arr[new_arr_idx]
                    new_arr_idx += 1
                    if new_arr_idx >= len(new_arr):
                        exit = False
                        break

        # 우 상
        i += 1
        for j in range(2):
            if exit == False:
                break
            if j == 0:
                for _ in range(i):
                    row_idx += 1
                    arr[col_idx][row_idx] = new_arr[new_arr_idx]
                    new_arr_idx += 1
                    if new_arr_idx >= len(new_arr):
                        exit = False
                        break
            else:
                for _ in range(i):
                    col_idx += -1
                    arr[col_idx][row_idx] = new_arr[new_arr_idx]
                    new_arr_idx += 1
                    if new_arr_idx >= len(new_arr):
                        exit = False
                        break





print(ans_dict[1] * 1 + ans_dict[2] * 2 + ans_dict[3] * 3)


#####
# dir = ["left", "down", "right", "up"]
# zero_flag = False
# # while zero_flag and
# dir_idx = 0
# cnt = 0
# i = 1
# exit_flag = True
# while cnt < n*n or exit_flag:
#     for j in range(2):
#         if i % 2 == 1:
#             # 좌 하
#             if dir[dir_idx % 4] == 0:
#                 print("left")
#                 dir += 1
#             elif dir[dir_idx % 4] == 1:
#                 print("down")
#         else:
#             if dir[dir_idx % 4] == 2:
#                 print("right")
#             if dir[dir_idx % 4] == 3:
#                 print("up")
#             # 우 상
#         cnt += i
#         # 0이 연속 2번 나오면 while 그만 돈다.
#         if v == "0" and zero_flag:
#             zero_flag = False
#
#     i += 1