n = int(input())
#학생들 정보를 한번에 입력 받음
students = [list(map(int,input().split())) for _ in range(n**2)]
#table 0 으로 초기화 해둠
table = [[0] * n for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
#학생 수 만큼 for문을 돌리면 자리에 앉히자
for k in range(n**2):
    student = students[k]
    tmp =[]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                #빈칸과 좋아하는 수를 0으로 초기화한 후 시작
                like=0
                blank=0
                #상하좌우 확인
                for l in range(4):
                    nr,nc = i + dr[l], j+dc[l]
                    #범위 내에서만
                    if 0<=nr <n and 0<=nc <n:
                        #좋아하는 사람을 찾으면
                        if table[nr][nc] in student[1:]:
                            like +=1
                        #빈칸도 count
                        if table[nr][nc] ==0 :
                            blank +=1
                tmp.append([like,blank,i,j])
    #like와 blank는 내림차순으로, 행과 열은 오름차순으로 tmp를 sort 해준후
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    table[tmp[0][2]][tmp[0][3]] = student[0]

result =0
#정렬을 해주면 쉽게 확인이 가능하다
students.sort()
for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if table[nr][nc] in students[table[i][j]-1][1:]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)


