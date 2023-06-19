x = int(input())  # 영수증 총 금액
n = int(input())  # 물건의 수

total = 0

for i in range(n):
    a, b = map(int, input().split())
    total += a*b

if(total == x):
    print("Yes")
else:
    print("No")
