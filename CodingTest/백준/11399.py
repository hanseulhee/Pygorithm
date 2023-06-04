n = int(input())
p = list(map(int, input().split()))
count = 0
sortP = sorted(p)

for i in range(1, n+1):
   count += sum(sortP[0:i])

print(count)