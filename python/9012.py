t = int(input())

for i in range(t):
    n = input()
    s = list(n) # 괄호를 문자열로 입력받아 리스트에 저장
    sum = 0
    for i in s: # 리스트 안에서 반복문
        if i == '(': # 여는 괄호일 경우
            sum += 1 # sum에 1을 더해주고
        elif i == ')': # 닫는 괄호일 경우
            sum -= 1 # sum에 1을 빼준다
        if sum < 0: # sum이 0보다 작을경우
            print('NO')
            break # 반복문 탈출
    if sum > 0:
        print('NO')
    elif sum == 0: #sum이 0일때 만 YES 출력
        print('YES')