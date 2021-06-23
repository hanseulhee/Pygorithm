s = input() # 단어 입력
alpha = [0]*26 # 알파벳 a ~ z 총 26개

for i in s:
    alpha[ord(i)-97] += 1

for i in alpha:
    print(i, end=' ')

