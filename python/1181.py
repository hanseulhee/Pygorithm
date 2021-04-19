n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
set_l = list(set(l)) # 중복 제거
set_l.sort()  # sort는 사전순으로 정렬해줌.
set_l.sort(key=lambda l: len(str(l)))  # 길이순으로 정렬해줌.


for j in set_l:
    print(j)