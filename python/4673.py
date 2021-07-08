self_num = set(range(1, 10001))
no_self_num = set()

for i in range(1, 10001):
    for j in str(i): # 하나하나 떼서 계산하기 위해 문자열로 바꿈
        i += int(j)
    no_self_num.add(i)

self_num = self_num - no_self_num # set 끼리 -가 가능함
for i in sorted(self_num):
    print(i)
