m = int(input())
result = 0

for i in range(1, m+1):
    n = list(map(int, str(i)))
    s = i + sum(n)
    if(s == m):
        result = i
        break
    # 이거 왜 안될까? 
    # if(i == m):
    #     print(0)

print(result)
