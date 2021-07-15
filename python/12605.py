n = int(input())

for i in range(1, n+1):
    l = input().split()
    print("Case #"+str(i)+":", " ".join(l[::-1]))
