n = int(input())
for i in range(n):
    num = list(map(int, input().split()))
    l = []
    for i in num:
        if i % 2 == 0:
            l.append(i)
    print(sum(l), min(l))


