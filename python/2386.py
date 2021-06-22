while True:
    n = input().split()
    alpha = n[0]
    if alpha == '#':
        break
    s = ''.join(n[1:])
    count = 0
    for alpha_s in s:
        if alpha == alpha_s.lower():
            count += 1
    print(alpha, count)

