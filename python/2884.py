H, M = map(int, input().split())

if M > 44:
    print(H, M-45) # 45분 이상일 경우 분에 45분을 빼서 잠을 더 자게함
elif M < 45 and H > 0:
    print(H-1, M+15) # 시간에서 1시간을 빼주고 분에 15분을 더하면 45분 뒤로 돌린 것이 됨
else:
    print(23, M+15)
