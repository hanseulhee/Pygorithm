n = int(input())

for i in range(n):
    # // 연산자를 통해 홀수일 경우와 짝수일 경우를 구분함
    print('* '*(n-n//2)) # 첫째 줄
    print(' *'*(n//2)) # 둘째 줄
