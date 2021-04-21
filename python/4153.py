while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break
    if a>b>c:
        big_number = a
        a_number = b
        b_number = c
    elif a < b < c:
        big_number = c
        a_number = a
        b_number = b
    elif a< c< b:
        big_number = b
        a_number = a
        b_number = c

    multiplication_a = a_number ** 2
    multiplication_b = b_number ** 2

    biggest_number = big_number ** 2

    sum_number = multiplication_a + multiplication_b


    if sum_number == biggest_number:
        print("right")

    else:
        print("wrong")


