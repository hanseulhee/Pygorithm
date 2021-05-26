n = input()
alpha = range(97, 123) # 아스키코드 숫자 범위
# range 메소드는 list 객체를 반환함 굳이 list로 안감싸줘도 됨 !

for x in alpha:
    print(n.find(chr(x)))