from collections import defaultdict


class FireBall:
    def __init__(self, r, c, m, s, d) -> None:
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d

    def move(self, s, d):
        for _ in range(s):
            nr = self.r + dr[d]
            nc = self.c + dc[d]
            if nr < 0:
                nr = N - 1
            if nr > N - 1:
                nr = 0
            if nc < 0:
                nc = N - 1
            if nc > N - 1:
                nc = 0
            self.r, self.c = nr, nc


def count_mass(fireball_list):
    return sum([fireball.m for fireball in fireball_list])


def unite_and_divide(fireball_list, fireball_idx_list, new_fireball_list):
    mass_sum, speed_sum, dir_even, dir_odd = 0, 0, 0, 0
    for idx in fireball_idx_list:
        fireball = fireball_list[idx]
        mass_sum += fireball.m
        speed_sum += fireball.s
        if fireball.d % 2 == 0:
            dir_even += 1
        else:
            dir_odd += 1
    mass = mass_sum // 5  # ⌊(합쳐진 파이어볼 질량의 합)/5⌋
    if mass == 0:
        return new_fireball_list
    speed = speed_sum // len_pos_k  # ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
    if (dir_even == len_pos_k) or (dir_odd == len_pos_k):
        dirs = [0, 2, 4, 6]
    else:
        dirs = [1, 3, 5, 7]
    for dir in dirs:
        new_fireball_list.append(
            FireBall(fireball.r, fireball.c, mass, speed, dir))
    return new_fireball_list


global N, dr, dc
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
fireball_list = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # r, c 초깃값 정상위치 보장 -> move 수정 필X
    fireball_list.append(FireBall(r-1, c-1, m, s, d))

# PLAY
for _ in range(K):
    # 모든 파이어볼 이동
    for fireball in fireball_list:
        s, d = fireball.s, fireball.d
        fireball.move(s, d)

    # 한 칸에 2개 이상있는 파이어볼 조사
    POS = defaultdict(list)
    for i, fireball in enumerate(fireball_list):
        r, c = fireball.r, fireball.c
        POS[(r, c)].append(i)

    # 파이어볼 합체, 분배 후 새로운 fire_ball_list에 담기
    new_fireball_list = []
    for k in POS.keys():
        len_pos_k = len(POS[k])
        if len_pos_k >= 2:
            new_fireball_list = unite_and_divide(
                fireball_list, POS[k], new_fireball_list)
        else:
            idx = POS[k][0]
            fireball = fireball_list[idx]
            new_fireball_list.append(fireball)

    # 업데이트
    fireball_list = new_fireball_list[:]

# 파이어볼들 질량의 합 계산
ans = count_mass(fireball_list)
print(ans)
