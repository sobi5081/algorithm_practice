import sys
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(bmap, w, h):
    fvisited = [[-1 for j in range(w)] for i in range(h)]
    svisited = [[-1 for j in range(w)] for i in range(h)]
    fire_queue = deque()
    sang_queue = deque()

    for i in range(h):
        for j in range(w):
            if bmap[i][j] == "*":
                fvisited[i][j] = 0
                fire_queue.append((i, j))
            if bmap[i][j] == "@":
                sang_queue.append((i, j, 0))
    tmp1 = 1
    tmp2 = 1
    while(fire_queue):
        if len(fire_queue) == 0:
            break
        #print(fire_queue)
        fv = fire_queue.popleft()

        #print(tmp1, "fire!!!!!!!!!!!!!!")
        tmp1 += 1
        #print("f",fv[0], fv[1])
        for i in range(4):
            fnx = fv[0] + dx[i]
            fny = fv[1] + dy[i]

            if fnx >= h or fny >= w or fnx < 0 or fny < 0:
                continue

            if bmap[fnx][fny] == "#" or fvisited[fnx][fny] >= 0:
                continue
            #print(fnx, fny)
            fire_queue.append((fnx, fny))
            fvisited[fnx][fny] = fvisited[fv[0]][fv[1]] + 1
            #print(fvisited)

    while(sang_queue):
        sv = sang_queue.popleft()
        #print(tmp2, "sang@@@@@@@@@@@@@@@@@@@@@@@@")
        tmp2 += 1
        for i in range(4):
            snx = sv[0] + dx[i]
            sny = sv[1] + dy[i]
            if snx >= h or sny >= w or snx < 0 or sny < 0:
                print(sv[2]+1)
                return
            if svisited[snx][sny] == 1:
                continue
            #print(snx, sny)
            if bmap[snx][sny] == "#" : #or svisited[snx][sny] == 1 or fvisited[snx][sny] == 1:
                #print("벽")
                continue
            if svisited[snx][sny] == 1:
                #print("상근")
                continue
            if (fvisited[snx][sny] <= sv[2] + 1 and fvisited[snx][sny] > 0) or fvisited[snx][sny] == 0:
                #print("불")
                continue

            # print(fvisited[snx][sny])
            # print(fvisited)
            # print(fvisited)

            sang_queue.append((snx, sny, sv[2]+1))
            svisited[snx][sny] = 1

    print("IMPOSSIBLE")
    return


k = int(input())
for tt in range(k):
    w, h = map(int, sys.stdin.readline().split())

    bmap=[]
    for i in range(h):
        bmap.append(sys.stdin.readline()[:-1])

    bfs(bmap, w, h)