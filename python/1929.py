from math import sqrt

m, n = map(int, input().split())
l = []
for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        l.append(i)
    else:
        for j in range(2, int(sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            l.append(i)

for i in sorted(l):
    print(i)
