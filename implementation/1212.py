import sys

def change(num,first = False):
    arr=''
    while num:
        arr += str(num%2)
        num //=2
    while len(arr) <3:
        arr += '0'
    idx =3
    if first:
        #첫번째 숫자라면 앞에 0을 없애야함
        #idx 숫자로 이진수 뒤에 숫자 부터 시작해서 1을 만나면 종료
        while idx>1 and arr[idx-1] =='0':
            idx -=1
    #idx까지 역순으로 출력한다.
    return arr[:idx][::-1]
#개행문자 제거해서 입력을 받는다.
n= sys.stdin.readline().rstrip()

isFirst= True
for i in range(len(n)):
    print(change(int(n[i]),isFirst),end='')
    isFirst=False