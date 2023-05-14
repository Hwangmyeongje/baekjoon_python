import sys
T = int(input())
for i in range(T):
   N = int(input())
   rank = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
   rank.sort()
   result =1
   top = rank[0][1]
   for j in range(1,N):
      if rank[j][1] < top:
         result +=1
         top = rank[j][1]
   print(result)



