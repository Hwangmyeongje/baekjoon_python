def fill_star(n,x,y):
    if n == 1:
        star[x][y] = '*'
        return
    lens = 4 * n - 3
    for i in range(lens):
        star[x][y+i] = '*'
        star[x+i][y] = '*'
        star[x+lens-1][y+i] = '*'
        star[x+i][y+lens-1] = '*'
    fill_star(n-1,x+2,y+2)


n = int(input())
lens = 4*n -3
star = [[' '] * lens for _ in range(lens)]
fill_star(n,0,0)
#join 함수는 리스트를 문자열로 변환해주는 함수이다.
for s in star:
    print(''.join(s))
# for i in range(lens):
#     for j in range(lens):
#         print(star[i][j], end="")
#     print()
#n이 줄어들수록 x,y 2만큼 증가가 된다.
#N번째의 결과는 4*n-3크기다