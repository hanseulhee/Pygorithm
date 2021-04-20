n = int(input())
l = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    l.append((age, name))

l.sort(key = lambda x: x[0])

for x in l:
    print(x[0], x[1])
