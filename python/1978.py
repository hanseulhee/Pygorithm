n = int(input())
l = list(map(int, input().split()))
result_count = 0

for i in l:
    count = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        result_count += 1
print(result_count)

