l = []
r = list(range(1, 31))

for i in range(28):
    s = int(input())
    l.append(s)

result = set(r) - set(l)
print('\n'.join((map(str, sorted(result)))))

