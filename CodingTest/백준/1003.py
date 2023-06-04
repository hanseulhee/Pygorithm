t = int(input())

for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    x = 0

    for _ in range(n):
        x = one
        one = one + zero
        zero = x
    print(zero, one)
