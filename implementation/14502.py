from collections import deque
import copy
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    virus = deque()
    #deepcopy시 원본 데이터에 영향x
    virus_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if virus_graph[i][j] == 2:
                virus.append((i,j))
    #바이러스를 뿌린다.
    while virus:
        x,y = virus.popleft()
        #상하좌우
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #인접한 곳이 0이면 2로 바꿔주고 virus_graph에 넣어준다.
            if 0<=nx<N and 0<=ny<M and virus_graph[nx][ny] == 0:
                virus_graph[nx][ny]=2
                virus.append((nx,ny))
    global result
    cnt=0
    for i in range(N):
        for j in range(M):
            if virus_graph[i][j] == 0:
                cnt +=1
    result = max(result,cnt)
#벽을 만든다. 이미 확인했던 부분을 중복 제거하면 best [1,2][2,1][2,2]와 [2,1][1,2][2,2]
#다음에는 중복제거를 해보자
def wall(cnt):
    if cnt ==3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] =1
                wall(cnt+1)
                graph[i][j] =0

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
result =0
wall(0)
print(result)