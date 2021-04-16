n = list(map(int, input().split()))
sort_n = sorted(n)
desc_n = sorted(n, reverse=True)

if n == sort_n:
    print('ascending')
elif n == desc_n:
    print('descending')
else:
    print('mixed')

