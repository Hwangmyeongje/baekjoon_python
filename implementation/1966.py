import sys
from collections import deque
input = sys.stdin.readline

t= int(input())

for i in range(t):
    n,m= map(int,input().split())
    queue = deque(list(map(int,input().split())))
    # cnt로 몇 번째로 인쇄되는지 확인
    cnt =0
    #m의 인덱스를 그때그때 초기화 하면서 m이 0인 순간에 front랑 best가 같다면 m인덱스 원소가 젤 앞에 있는거임
    while queue:
        #가중치가 가장 큰 값과 큐의 맨 앞 값을 비교한다.
        best_important = max(queue)
        front = queue.popleft()
        #큐의 front를 뽑으면 m을 한 칸 당긴다.
        m -=1
        if best_important == front:
            cnt +=1
            if m<0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m<0:
                m =len(queue)-1




# 4 2
# m=2
# 1 2 3 4
#
# m=1
# 2 3 4 1
#
# m =0
# 3 4 1 2
#
# m = 3
# 4 1 2 3
#
# m = 2
# 1 2 3
#
# m = 1
# 2 3 1
#
# m = 0
# 3 1 2
#
# m= -1
# 3 출력