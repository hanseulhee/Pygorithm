n = int(input())
num = 2 # 소인수분해이므로 num을 2로 함

while n != 1: # n이 1이 됐을 때 while문 탈출
    if n % num == 0: # 나머지가 0이면 n을 num으로 나눠 n에 저장한다. 그 후 num 출력
        n = n / num
        print(num)
    else: # 나머지가 0이 아니면 num에 1 증가시킴
        num = num+1
