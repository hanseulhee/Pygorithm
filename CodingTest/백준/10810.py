n, m = map(int, input().split())

x = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())  # 부터, 까지, 몇번 공
    for y in range(i, j+1):
        x[y - 1] = k
for i in range(n):
    print(x[i], end=" ")
