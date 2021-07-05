n = int(input())
sing = 1
count = 0 # 몇 초가 걸릴 지 카운트

while n > 0:
    if sing > n:
        sing = 1 # 1부터 게임을 다시 시작
    n -= sing # 부른 노래 수 만큼 새의 수 감소
    sing += 1
    count += 1

print(count)

