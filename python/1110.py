N = M = int(input())
count = 0

while True:
    ten = N//10
    one = N % 10
    sum = ten + one
    count += 1
    N = int(str(N % 10)+str(sum % 10))

    if(M==N):
        break
print(count)


