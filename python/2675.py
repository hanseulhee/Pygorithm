a = int(input()) # 입력 횟수

for i in range(a):
    r, s = input().split()  # 몇번 반복 # 문자열 입력
    m = int(r)
    l = list(s)

    for j in l:
        p = j*m
        print(p, end='')
    print()





