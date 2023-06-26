n = int(input())
count = 0
r = set()

for i in range(n):
    context = input()
    if (context == "ENTER"):
        count += len(r)
        r = set()
    else:
        r.add(context)

count += len(r)

print(count)
