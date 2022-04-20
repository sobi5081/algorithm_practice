import sys
from collections import deque

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(field):
    queue = deque()
    count = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1 and visited[i][j] == 0:
                queue.append((i, j))
                count += 1
                visited[i][j] = 1
                while(queue):
                    v = queue.popleft()
                    for d in range(4):
                        nx = v[0] + dx[d]
                        ny = v[1] + dy[d]

                        if nx >= n or ny >= m or nx < 0 or ny < 0:
                            continue
                        if visited[nx][ny] == 1 or field[nx][ny] == 0:
                            continue
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
    print(count)

for turn in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    cabbage = []
    for i in range(k):
        cabbage.append(list(map(int, sys.stdin.readline().split())))

    field = [[0 for j in range(m)] for i in range(n)]
    visited = [[0 for j in range(m)] for i in range(n)]

    for i in range(len(cabbage)):
        field[cabbage[i][1]][cabbage[i][0]] = 1
    bfs(field)




