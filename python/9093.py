t = int(input())

for i in range(t):
    n = input().split()
    for j in n:
        print("".join(j[::-1]), end=" ")