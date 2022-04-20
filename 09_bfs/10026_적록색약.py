import sys
from collections import deque

n = int(input())
RGB = []
for i in range(n):
    RGB.append(sys.stdin.readline()[:-1])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs1(rgb):
    queue = deque()
    count = 0
    for p in range(n):
        for q in range(len(rgb[0])):
            if visited[p][q] == 0:
                queue.append((p, q, rgb[p][q]))
                count = count + 1
                while(queue):
                    v = queue.popleft()
                    for i in range(4):
                        nx = v[0] + dx[i]
                        ny = v[1] + dy[i]
                        if nx >= n or ny >= len(rgb[0]) or nx <0 or ny < 0:
                            continue
                        if rgb[nx][ny] != v[2] or visited[nx][ny] == 1:
                            continue
                        queue.append((nx, ny, rgb[nx][ny]))
                        visited[nx][ny] = 1
    return count


def bfs2(rgb):
    queue = deque()
    count = 0
    for p in range(n):
        for q in range(len(rgb[0])):
            if visited[p][q] == 0:
                queue.append((p, q, rgb[p][q]))
                count = count + 1
                while(queue):
                    v = queue.popleft()
                    for i in range(4):
                        nx = v[0] + dx[i]
                        ny = v[1] + dy[i]
                        if nx >= n or ny >= len(rgb[0]) or nx < 0 or ny < 0:
                            continue
                        if visited[nx][ny] == 1:
                            continue
                        if (v[2] == "R" or v[2] == "G") and rgb[nx][ny] == "B":
                            continue
                        if v[2] == "B" and (rgb[nx][ny] == "R" or rgb[nx][ny] == "G"):
                            continue
                        queue.append((nx, ny, rgb[nx][ny]))
                        visited[nx][ny] = 1
    return count


visited = [[0 for j in range(len(RGB[0]))] for i in range(n)]
res = ""
res = res + str(bfs1(RGB)) + " "
visited = [[0 for j in range(len(RGB[0]))] for i in range(n)]
res = res + str(bfs2(RGB))
print(res)
