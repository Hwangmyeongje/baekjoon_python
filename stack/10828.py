import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    #명령어와 정수를 공백을 기준으로 나눠 입력 받음
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])