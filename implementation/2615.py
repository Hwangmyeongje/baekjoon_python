import sys

found = False
concave=[]
for _ in range(19):
    concave.append(list(map(int,sys.stdin.readline().split())))

#우 하 위대각, 아래 대각
dx = [0,1,-1,1]
dy = [1,0,1,1]
def search(x,y):
    global found
    color = concave[x][y]
    #4가지 방향으로 탐색 해야 되니 4번 돌림
    for k in range(4):
        cnt =1
        nx = x+dx[k]
        ny = y+dy[k]
        #오목이 되는지 확인하는 while문
        while 0<=nx<19 and 0<=ny<19 and color == concave[nx][ny]:
            cnt+=1
            #오목이 된다면 6목인지 확인해야함
            #전값과 다음값 확인해보면됨
            if cnt == 5:
                #시작점 전 값 확인
                if 0<=x-dx[k] <19 and 0 <= y-dy[k]<19 and color == concave[x-dx[k]][y-dy[k]]:
                    break
                #끝점 다음 값 확인
                if 0<=nx+dx[k] <19 and 0<= ny+dy[k]<19 and color == concave[nx+dx[k]][ny+dy[k]]:
                    break
                #육목이 아니면 출력하고 끝낸다
                print(color)
                # 좌표
                print(x+1,y+1)

                found = True
                sys.exit(0)

            nx += dx[k]
            ny += dy[k]




#0이 아닌 값을 찾으면 search 함수 부름
for i in range(19):
    for j in range(19):
        if concave[i][j] != 0:
            search(i,j)

if found == False:
    print(0)