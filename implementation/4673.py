#생성자를 만드는 함수
#생성자를 만들어서 n을 str로 바꿔준 후에 자리수별로 더한다.
def d(n):
   for i in str(n):
       #n += int(i) == n = n + int(i)
       n += int(i)
   return n
#중복을 제거하기 위해 집합으로 만들어 준다
#셀프 넘버가 아닌 수들
remove_list = set()
#1부터 10000까지 돌면서 셀프넘버가 아닌 수들은 추가해준다.
for i in range(1,10001):
    temp = d(i)
    if temp <=10000:
        remove_list.add(d(i))

for i in range(1,10001):
    if i not in remove_list:
        print(i)