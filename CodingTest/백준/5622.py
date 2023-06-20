text = list(input())
time = 0

arr = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

for i in text:
    for j in arr:
        if i in j:
            time += arr.index(j) + 3


print(time)
