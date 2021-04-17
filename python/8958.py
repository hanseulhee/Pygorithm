n = int(input())

for i in range(n):
    z = input()
    sum = 0
    count = 0
    for j in z:
        if j == 'O':
            count += 1
        else:
            count = 0
        sum += count
    print(sum)
