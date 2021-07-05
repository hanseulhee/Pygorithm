n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0: # 나머지가 0인 경우
        count += n // 5
        print(count)
        break
    n -= 3
    count += 1 # 설탕이 5의 배수가 될 때까지 n(설탕)-3 , count(봉지)+1
else:
    print(-1)



