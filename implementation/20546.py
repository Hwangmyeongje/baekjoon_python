cash = int(input())
stock_price = list(map(int,input().split()))
j_price = cash
s_price = cash
#준현,성민 주식 수
j_cnt = 0
s_cnt =0
up_cnt =0
down_cnt = 0
k=-1
for i in range(len(stock_price)):
    k +=1
    if j_price >= stock_price[i]:
        j_cnt += j_price // stock_price[i]
        j_price -= stock_price[i] *j_cnt
    if k>0:
        if stock_price[i-1] < stock_price[i]:
            up_cnt +=1
            down_cnt =0
        elif stock_price[i-1] > stock_price[i]:
            down_cnt +=1
            up_cnt =0
        else:
            up_cnt = 0
            down_cnt =0
    #3일 연속 상승 시 전량 매도
    if up_cnt >= 3:
        s_price += s_cnt * stock_price[i]
        s_cnt = 0
    #3일 연속 하락 시 전량 매수
    elif down_cnt >=3:
        temp_cnt = s_price // stock_price[i]
        s_cnt += temp_cnt
        s_price -= stock_price[i] * temp_cnt

j_price = j_price + stock_price[len(stock_price)-1] * j_cnt
s_price = s_price + stock_price[len(stock_price)-1] * s_cnt

if j_price > s_price:
    print("BNP")
elif j_price < s_price:
    print("TIMING")
else: print("SAMESAME")