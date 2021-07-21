c = int(input())

for i in range(c):
    n = list(map(int, input().split()))
    average = sum(n[1:])/n[0] # 평균
    count = 0

    for j in n[1:]: # 평균을 넘는 학생 카운트
        if j > average:
            count += 1

    result = (count / n[0]) * 100 # 카운트한 걸 학생 수만큼 나누어주고 100곱함
    print('%.3f' % result + '%') # 소수점 3번째 자리까지 출력