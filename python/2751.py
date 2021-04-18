n = int(input())
l = []

for i in range(n):
    num = int(input())
    l.append(num)


for j in sorted(l):
    print(j)

# 시간 초과 나와서 못함 ㅠㅠ
# set으로 중복제거 sorted로 오름차순 정렬 join으로 문자열로 연결해줌

# a = sorted(set(l))
#
# a_str = '\n'.join(a)
# print(a_str)


