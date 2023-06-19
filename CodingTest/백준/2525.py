a, b = map(int, input().split())

c = int(input())

a += c // 60
b += c % 60


if (b >= 60):
    b -= 60  # 60을 빼줌
    a += 1  # 한시간 증가

if(a >= 24):
    a -= 24 # 24시가 넘으면 24 빼기

print(a, b)
