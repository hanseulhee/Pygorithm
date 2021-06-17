n = input()

for i in range(0, len(n), 10): # range(시작값, 종료값, step) > 인덱스 0부터 n길이-1 까지, 10씩!
    # n을 i부터 i에서 10 더한 값만큼 끊어서 슬라이싱
    print(n[i:i + 10]) # n[시작값:원하는 종료값 + 10]
