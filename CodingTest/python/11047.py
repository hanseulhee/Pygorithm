n, k = map(int, input().split())
array = []
count = 0
for _ in range(n):
    a = int(input())
    array.append(a)

for i in reversed(range(n)):
    count += k // array[i] # 몫
    k = k % array[i] # 나머지

print(count)