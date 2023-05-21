n = int(input())
score_list = list(map(int,input().split()))
max_score = max(score_list)
avg =0
for i in range(len(score_list)):
    score_list[i] = score_list[i]/max_score*100
    avg += score_list[i]
avg /= len(score_list)
print(avg)