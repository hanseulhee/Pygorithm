N = M = int(input())
count = 0

while True:
    sum = (N//10) + (N % 10)
    count += 1
    N = int(str(N % 10)+str(sum % 10))
    if(M==N):
        break
print(count)


