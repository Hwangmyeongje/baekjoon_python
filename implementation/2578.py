import sys
input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(5)]
#진행자가 부르는 숫자를 1차원 배열로 받아야 4중 for문을 안 할 수 있음
mc = []
for _ in range(5):
    mc += list(map(int,input().split()))


def bingo():
    bingo_cnt = 0
    #가로 확인
    for x in arr:
        if x.count(0) == 5:
            bingo_cnt +=1
    #세로 확인
    for i in range(5):
        tmp = 0
        for j in range(5):
            #세로를 확인하기 위해서는 행을 늘려가면서 비교해야함
            if arr[j][i] == 0:
                tmp +=1 #세로 한줄에 0인 개수를 세기 위해서 tmp를 이용한다.
        #tmp가 5라면 bingo
        if tmp == 5:
            bingo_cnt +=1
    #왼쪽위에서 시작하는 대각선과, 오른쪽 위에서 시작하는 대각선
    diagonal1 = 0
    diagonal2 = 0
    #왼쪽 위에서 시작 대각선
    for i in range(5):
        if arr[i][i] == 0:
            diagonal1 +=1
    #오른쪽 위에서 시작 대각선
    for i in range(5):
        if arr[i][4-i] == 0:
            diagonal2 +=1
    if diagonal1 == 5:
        bingo_cnt +=1
    if diagonal2 == 5:
        bingo_cnt += 1
    return bingo_cnt

call = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            #사회자가 부를때마다 그 번호를 0으로 만든다
            if mc[k] == arr[i][j]:
                arr[i][j] = 0
                call +=1
            #최소 3개의 빙고를 만들기 위해서는 12개의 원소가 필요하다
    if call >=12:
        result = bingo()
        if result >= 3: #빙고함수를 불러서 값이 3이상이라면
            print(k+1)
            exit()

