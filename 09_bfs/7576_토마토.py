import sys
from collections import deque

m, n = sys.stdin.readline().split()
m, n = int(m), int(n)

tomato_field = []
for i in range(n):
    tomato_field.append(list(map(int,sys.stdin.readline().split())))

dist = [[0 for j in range(m)] for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(field):
    queue = deque()
    max = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                queue.append((i, j))
            elif field[i][j] == 0:
                dist[i][j] = -1
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if dist[nx][ny] >= 0 :
                continue
            queue.append((nx, ny))
            dist[nx][ny] = dist[v[0]][v[1]] + 1
            if dist[nx][ny] > max:
                max = dist[nx][ny]

    # for i in dist:
    #     for j in i:
    #         if j == -1:
    #             print(-1)
    #             return
    for i in dist:
        if -1 in i:
            print(-1)
            return

    if max == 0:
        print(0)
        return
    else:
        print(max)
        return

bfs(tomato_field)