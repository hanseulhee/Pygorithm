import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split()) # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    num = N//H +1 # 각 층의 방 번호
    floor = N % H # 객실의 층
    if N % H == 0: # H의 배수이면
        num = N//H
        floor = H
    print(f'{floor*100+num}')

# 손님이 들어가는 층수는 몇 번째 손님을 높이로 나눈 나머지.
# 손님이 들어가는 방 번호는 몇 번째 손님을 높이로 나눈 몫의 + 1.