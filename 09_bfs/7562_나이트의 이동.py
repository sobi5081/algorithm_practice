import sys
from collections import deque

n = int(input())

dx = [-2, -1, 1, 2, 1, -2, 2, -1]
dy = [-1, -2, 2, 1, -2, 1, -1, 2]

def bfs(dist):
    queue = deque()
    queue.append((loc[0][0], loc[0][1]))
    dist[loc[0][0]][loc[0][1]] = 0

    while(queue):
        v = queue.popleft()

        for i in range(8):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx >= k or ny >= k or nx < 0 or ny < 0: #범위를 벗어나면 continue
                continue

            if dist[nx][ny] == -1:#방문한 적이 없으면
                dist[nx][ny] = dist[v[0]][v[1]] + 1
                queue.append((nx, ny))

    print(dist[loc[1][0]][loc[1][1]])

for i in range(n):
    k = int(input())
    loc = []
    for i in range(2):
        loc.append(list(map(int, sys.stdin.readline().split())))
    if loc[0][0] == loc[1][0] and loc[1][0] == loc[1][1]:
        print(0)
        continue

    dist = [[-1 for j in range(k)] for i in range(k)]

    bfs(dist)
