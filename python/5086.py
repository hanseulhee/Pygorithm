# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0: # n이랑 m이 0일 때 탈출!
#         break
#     if m % n == 0: # 런타임에러 때문에 이렇게 해줌
#         print("factor")
#     elif n % m == 0:
#         print("multiple")
#     else:
#         print("neither")

while True:
    n, m = map(int, input().split())
    try:
        if n == 0 and m == 0:
            break
        if m % n == 0:
            print("factor")
        elif n % m == 0:
            print("multiple")
        else:
            print("neither")
    except ZeroDivisionError:
        print("ZeroDivisionError이지롱")

