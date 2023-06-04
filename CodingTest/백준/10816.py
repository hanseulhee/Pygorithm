import sys

N = int(sys.stdin.readline())
numCard = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
countCard = list(map(int, sys.stdin.readline().split()))

count = {}

for i in numCard:
    if(i in count):
        count[i] += 1
    else:
        count[i] = 1

for j in countCard:
    if j in count:
        print(count[j], end=" ") # 존재하는 숫자라면
    else:
        print(0, end=" ") # 존재하지 않는 숫자라면 0을 출력한다.