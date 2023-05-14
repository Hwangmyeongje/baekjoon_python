n= int(input())
load_list = list()
liter_list = list()
load_list = list(map(int,input().split()))
liter_list = list(map(int,input().split()))
result =0
for i in range(n-1):
    if(liter_list[i] < liter_list[i+1]):
        liter_list[i+1] = liter_list[i]
for i in range(n-1):
    result += liter_list[i] * load_list[i]
print(result)


