import sys
input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])

l_sort = sorted(l)

for i in range(n):
    print(l_sort[i][0], l_sort[i][1])

