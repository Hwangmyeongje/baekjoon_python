n,k = map(int,input().split())
coin_list =list()
for i in range(n):
    coin_list.append(int(input()))
count =0
coin_list.sort(reverse=True)
for i in range(n):
    count += k//coin_list[i]
    k= k%coin_list[i]
print(count)
