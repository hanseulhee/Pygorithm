import sys
n = int(sys.stdin.readline())
array = []
dp = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))


if n == 1:
    print(array[0])
elif n == 2:
    print(array[0] + array[1])
else:
    dp.append(array[0])
    dp.append(max(array[0]+array[1], array[1]))
    dp.append(max(array[0] + array[2], array[1]+array[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2] + array[i], dp[i-3] + array[i] + array[i-1]))

    print(dp[-1])
