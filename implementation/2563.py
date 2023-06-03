import sys
imput = sys.stdin.readline
n = int(input())
paper = [[0] * 101 for i in range(101)]
cp_list= [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
       cp_x = cp_list[i][0]
       cp_y = cp_list[i][1]
       for j in range(10):
           for k in range(10):
               paper[cp_x+j][cp_y+k] = 1


result =0
for i in paper:
    result += sum(i)
print(result)
