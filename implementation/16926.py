import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    #사각형의 수
    for i in range(min(n,m)//2):
        #돌려지는 배열의 가장 첫 번째 인덱스
        x,y = i,i
        temp = arr[x][y]
        #밑으로 이동
        for j in range(i+1,n-i):
            x = j
            prev_data = arr[x][y]
            arr[x][y] = temp
            temp = prev_data
        #우로 이동
        for j in range(i+1,m-i):
            y = j
            prev_data = arr[x][y]
            arr[x][y] = temp
            temp = prev_data
        #위로 이동
        for j in range(n-i-1,i,-1):
            x= j-1
            prev_data = arr[x][y]
            arr[x][y] = temp
            temp = prev_data
        #좌로 이동
        for j in range(m-i-1,i,-1):
            y = j-1
            prev_data = arr[x][y]
            arr[x][y] = temp
            temp = prev_data



for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
