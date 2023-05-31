number = int(input())
line = 0
last_index =0
#last_index= 마지막 인덱스 라인당 수가 1,2,3 증가함
while number > last_index:
    line +=1
    last_index += line
    print(last_index)

print(line)
if line %2 == 0:
    up = line - (last_index - number)
    down = last_index - number +1
else:
    up = last_index - number +1
    down = line - (last_index -number)

print(up,down, sep="/")
