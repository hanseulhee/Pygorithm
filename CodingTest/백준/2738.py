A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)


for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for row in range(N):
    for column in range(M):
        print(A[row][column] + B[row][column], end=" ")
    print()
