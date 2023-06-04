import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    array.append([y, x])

sortArray = sorted(array)

for i in range(n):
    print(sortArray[i][1], sortArray[i][0])