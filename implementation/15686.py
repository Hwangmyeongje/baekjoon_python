from itertools import combinations
import sys
n,m = map(int,sys.stdin.readline().split())
house =[]
chicken =[]
arr = []
#무한대로 설정
result = float('inf')
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
#도시의 치킨 거리의 최솟값을 출력
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))
#chickn을 m개 조합해서 뽑아낸다.
for chikCombi in combinations(chicken,m):
    #치킨 거리의 합을 total_dis에 저장한다.
    total_dis = 0
    #집에서부터 가장 가까운 치킨 거리를 구한다음에 total_dis에 합해준다.
    for r1,c1 in house:
        dis = float('inf')
        #집에서부터 가장 가까운 치킨 거리를 구하는 for문
        for r2,c2 in chikCombi:
            dis = min(dis,abs(r1-r2)+abs(c1-c2))
        total_dis += dis
    #치킨집 조합마다 보면서 최소 거리를 저장한다.
    result = min(result,total_dis)

print(result)


