n = int(input())
rope_list =list()
w =0
k = 0
max_w = 0
for i in range(n):
    rope_list.append(int(input()))
rope_list.sort(reverse=True)
for i in rope_list:
    k+=1
    m = i*k
    if(max_w < m):
        max_w = m

print(max_w)