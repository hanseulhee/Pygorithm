T = int(input())

for _ in range(T):
    s = int(input())
    price = s
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        price += q * p
    print(price)