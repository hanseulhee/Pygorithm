n = int(input())
hansu = 0
for i in range(1, n+1):
    if i <= 99:
        hansu += 1
    else:
        n_split = list(map(int, str(i)))
        if n_split[0] - n_split[1] == n_split[1] - n_split[2]:
            hansu+=1

print(hansu)
