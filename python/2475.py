n = input().split()
l = list(map(int, n))
r = []

for i in l:
    square = i*i
    r.append(square)

result = sum(r) % 10

print(result)

