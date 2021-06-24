t = int(input())

for i in range(t):
    s = input()
    n = str(int(s) + int(s[::-1])) # 원래 수와 뒤집은 수를 합한 수
    if n == n[::-1]: # 좌우 대칭이 되는가?
        print("YES")
    else:
        print("NO")
