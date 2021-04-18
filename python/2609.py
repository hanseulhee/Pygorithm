n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)


def gcd(n1, n2):
    while n2 > 0:
        n1, n2 = n2, n1 % n2
    return n1
