N, M = map(int, input().split())

array = []
count = []

for _ in range(N):
    array.append(input())

for i in range(N-7):  # 행
    for j in range(M-7):  # 열
        WCount = 0  # W
        BCount = 0  # B
        for row in range(i, i+8):
            for column in range(j, j+8):
                if(row + column) % 2 == 0:
                    if array[row][column] != "W":
                        WCount += 1
                    if array[row][column] != "B":
                        BCount += 1
                else:
                    if array[row][column] != "B":
                        WCount += 1
                    if array[row][column] != "W":
                        BCount += 1
        count.append(min(WCount, BCount))

print(min(count))