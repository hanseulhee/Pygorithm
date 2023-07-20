# 런타임 에러
# n = int(input())

# for _ in range(n):
#     x = list(map(int, input().split()))

# sortedArr = sorted(list(set(x)))
# dic = {sortedArr[i]: i for i in range(len(sortedArr))}

# for i in x:
#     print(dic[i], end=' ')

import sys

n = int(sys.stdin.readline())
x = list(map(int, input().split()))

sortedArr = sorted(list(set(x)))
dic = {sortedArr[i]: i for i in range(len(sortedArr))}

for i in x:
    print(dic[i], end=' ')
