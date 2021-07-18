t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    r = min(a, b)
    for j in range(1, r+1):
        if a % j == 0 and b % j == 0:
            GCD = j # 최대공약수
    LCM = a*b//GCD # 최대공배수
    print(LCM)
