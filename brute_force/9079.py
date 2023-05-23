def find_arr(arr):
    global result
    #bit_mask는 0부터 255까지 돈다.
    for bit_mask in range(2 ** 8):
        copy_arr = [row[:] for row in arr]
        #이진수로 바꿔준 후 0b를 제외한 나머지 부분을 선택한 뒤에 1의 개수를 세준다.
        #변경 횟수를 나타내며, 나중에 최소 변경 횟수를 찾기 위해 사용된다.
        change_bit = str(bin(bit_mask))[2:].count('1')
        #이전에 찾은 최소 변경 횟수보다 많다면 해당 반복을 건너 뛴다.
        if result < change_bit:
            continue
        for row in range(3):
            if bit_mask & (1 << row):
                for col in range(3):
                    #요소의 값들 변경 1이면 0 0이면 1로
                    copy_arr[row][col] = (copy_arr[row][col] + 1) % 2

        for col in range(3):
            if bit_mask & (1 << (col + 3)):
                for row in range(3):
                    copy_arr[row][col] = (copy_arr[row][col] + 1) % 2

        if bit_mask & (1 << 6):
            for row in range(3):
                copy_arr[row][row] = (copy_arr[row][row] + 1) % 2

        if bit_mask & (1 << 7):
            for row in range(3):
                copy_arr[row][2 - row] = (copy_arr[row][2 - row] + 1) % 2

        sum_temp = sum(list(map(sum, copy_arr)))
        if sum_temp == 9 or sum_temp == 0:
            result = change_bit


T = int(input())

for tc in range(T):
    arr = []
    #result변수를 무한대 값으로 초기화
    result = float('inf')
    for _ in range(3):
        s = list(input().split())
        for i in range(3):
            if s[i] == 'T':
                s[i] = 1
            else:
                s[i] = 0
        arr.append(s)
    cnt = 0
    find_arr(arr)
    #result 무한대라면 -1 출력
    print(-1 if result == float('inf') else result)