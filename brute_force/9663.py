#위치가 유효한지 확인한다.
def check(x):
    #현재 위치 x와 이전 행 i의 열 값이 같다면 같은 열에 퀸이 위치한 것임
    #현재 위치x와 이전 행i 간의 차이와 열 간의 차이가 같다면, 같은 대각선의 퀸위 위치한 것임
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True
def dfs(x):
    global result
    if x == n:
        result+=1
        return
    else:
        for i in range(n):
            #x,i 좌표에 퀸을 놓은 것임
            #row[x] = x 행에 해당하는 열
            #row[0] =2 라면 첫 번째 행에 퀸을 두번 배치 하는 것
            row[x] = i
            if check(x):
                #배치 가능시 다음행으로 넘어간다.
                dfs(x+1)


n = int(input())
#퀸은 좌우상하 대각선에 다른 퀸이 없어야 한다
row = [0]*n
result = 0
dfs(0)
print(result)