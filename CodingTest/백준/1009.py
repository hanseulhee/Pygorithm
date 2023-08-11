# 시간 초과

# t = int(input())
# data = 0

# for _ in range(t):
#     a, b = map(int, input().split())
#     data = a**b
#     print(data % 10)

# 일의 자리수 규칙 적용

import sys

input = sys.stdin.readline

t = int(input())
a = []
b = []

for _ in range(t):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

for i in range(t):
    result = a[i] % 10

    if result == 0:
        print(10)
    elif result in [1, 5, 6]:
        print(result)
    elif result in [4, 9]:
        if b[i] % 2 == 0:
            print(result ** 2 % 10)
        else:
            print(result)
    else:
        if b[i] % 4 == 0:
            print(result ** 4 % 10)
        else:
            print(result ** (b[i] % 4) % 10)
