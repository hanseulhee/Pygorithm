from collections import deque

N, K = map(int, input().split())

queue = deque([])

for i in range(1, N+1):
    queue.append(i)  # 1부터 N까지 의 수를 queue에 담는다.
print("<", end="")

while queue:
    for i in range(K-1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end="")
    if queue:  # queue에 값이 있다면
        print(",", end=" ")
print(">")