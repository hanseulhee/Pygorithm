from math import sqrt

m = int(input())
n = int(input())
sum = 0 # 합
min = 0 # 최솟값

for i in range(m, n+1):
    if i == 1: # 1일 수도 있으니 조건을 달아줌
        continue
    elif i == 2: # 2는 소수이므로 조건을 달아줘야 함
        sum += i
        min = i
    else:
        for j in range(2, int(sqrt(i)+1)): # 2부터 i의 제곱근을 내림한 값+1
            if i % j ==0:
                break
        else: # i를 j로 나눴을 때 나머지가 0이 아니라면 i는 소수
            if sum == 0:
                min = i
            sum += i
if sum == 0: # 소수가 없을 경우
    print(-1)
else:
    print(sum)
    print(min)





