N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
N2 = N * N
x = 0
y = 0
dx = [1, 0, -1, 0]  # 하, ,우 상, 좌 순서로 이동
dy = [0, 1, 0, -1]
dir_idx = 0  # 방향 인덱스

while N2 > 0:
    arr[x][y] = N2
    if N2 == K:
        K_x = x
        K_y = y
    N2 -= 1


    if 0 <= x + dx[dir_idx] < N and 0 <= y + dy[dir_idx] < N and arr[x + dx[dir_idx]][y + dy[dir_idx]] == 0:
        x += dx[dir_idx]
        y += dy[dir_idx]
    else:
        dir_idx = (dir_idx + 1) % 4  # 방향 변경
        x += dx[dir_idx]
        y += dy[dir_idx]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
print(K_x+1,K_y+1)