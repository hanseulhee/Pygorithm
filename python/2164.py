from collections import deque

n = int(input())
de = deque()

for i in range(1, n+1):
    de.append(i)

while len(de) != 1:
    de.popleft()
    de.append(de.popleft())

print(de[0])