import math

# a: 올라가는 길이, b: 떨어지는 길이, v: 나무 높이
a, b, v = map(int, input().split())

day = math.ceil((v-a)/(a-b)) + 1 # ceil 함수 사용
print(day)