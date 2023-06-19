'''
시작    6:50
1. 달빛여우 최적 경로 구하기
2. 달빛늑대 최적 경로 구하기
1에서 시작한다.
시간초과 해결
'''
from collections import defaultdict, deque
import heapq
import pdb
import sys
n, m = map(int,sys.stdin.readline().split())
g = defaultdict(list)
for _ in range(m):
    a, b, d = map(int,sys.stdin.readline().split())
    g[a].append([b,d])
    g[b].append([a,d])
def dijkstra(v, s, adj):
    dist = [INF]*(v+1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap, [0,s])
    while heap:
        cost, node = heapq.heappop(heap)
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(heap, [c,n])
    return dist
def dijkstra_wolf(v, s, adj):
    dist = [[INF,INF] for _ in range(v+1)]
    dist[s][1] = 0
    heap = []
    heapq.heappush(heap, [0, s, False])
    while heap:
        cost, node, flag_slow = heapq.heappop(heap)
        if flag_slow:
            for n, c in adj[node]:
                n_c = c*2 + cost
                if float(n_c)<dist[n][1]:
                    dist[n][1] = n_c
                    heapq.heappush(heap, [n_c, n, False])
        else:
            for n, c in adj[node]:
                n_c = (c/2) + cost
                if n_c<float(dist[n][0]):
                    dist[n][0] = n_c
                    heapq.heappush(heap, [n_c, n, True])

    return dist
INF = int(1e9)
fox = dijkstra(n, 1, g)[2:]
wolf = dijkstra_wolf(n,1,g)[2:]
ans =0
for i, d_f in enumerate(fox):
    d_w = min(wolf[i][0], wolf[i][1])
    if d_f<d_w:
        ans +=1
print(ans)

    

