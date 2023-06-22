n, k = map(int, input().split())
x = sorted(list(map(int, input().split())))

x.sort(reverse=True)

print(x[k-1])
