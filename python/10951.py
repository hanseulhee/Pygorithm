import sys

lines = sys.stdin.readlines()

for line in lines:
    x, y = map(int, line.split())
    print(x+y)

