average = 0  # 평균
arr = []  # 배열
median = 0  # 중앙값

for _ in range(5):
    arr.append(int(input()))

arr.sort()
average = sum(arr) // 5
median = arr[2]

print(average, median)
