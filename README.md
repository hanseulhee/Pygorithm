## Problem Solving with Python



#### 21.04.15

- [BOJ 10951](../master/python/10951.py)

  A+B 출력, 입력이 끝날 때까지 받아오는 방법
  
  - sys.stdin.readlines() 
  
    파일의 끝 부분까지 한번에 가져옴, 마지막에 ctrl+d로 cli에 파일이 끝났음을 알려줘야함
    근데 이게 아래 방법보다 더 빠름
    
  - EOF
    
    입력 도중 파일의 끝을 만나면 EOFError가 발생 > 반복문에서 나옴
    
 
- [BOJ 11654](../master/python/11654.py)

    아스키코드 출력문제, ord(문자)와 chr(숫자) 함수로 해당하는 아스키코드를 출력함
    
    
#### 21.04.16

- [BOJ 11720](../master/python/11720.py)

  공백없는 숫자 N개의 합 구하는 문제, 
  map은 맵 오브젝트를 반환하기 때문에 list로 감싸줌
  
- [BOJ 2920](../master/python/2920.py)

  입력 값이 정렬일 경우와 뒤집어져있을 경우,
  sorted함수와 reverse사용
          
#### 21.04.17

- [BOJ 8958](../master/python/8958.py)

   for문과 if문 사용, 필요한 변수가 뭔지 정리해보고 계산식을 짜야겠다고 느낌

#### 21.04.18

- [BOJ 2675](../master/python/2675.py)

    문자열 반복, for문 사용. print()으로 줄바꿈함
    
- [BOJ 2751](../master/python/2751.py)

    오름차순 정렬문제, sorted를 이용해 오름차순으로 정렬해줌
    class 1 에센셜 완료! (～￣▽￣)～
    
#### 21.04.19

- [BOJ 2609](../master/python/2609.py)

    최대 공약수와 최소 공배수 출력문제, 
    
    유클리드 호제법
    
    a,b의 최대공약수 = GCD(a,b) = GCD(b,a%b)
    a%b를 r로 표현했을 때, r이 0이면 그때 b가 최대공약수.
    
    a,b의 최소공배수 = 최대공약수 * a/최대공약수 * b/최대공약수
    
- [BOJ 1181](../master/python/1181.py)

    단어 정렬문제, set으로 중복제거. sort로 사전순 정렬. len으로 길이 순으로 정렬함
    
#### 21.04.20

- [BOJ 10989](../master/python/10989.py)

    수 오름차순 정렬문제, 메모리 초과로 sys.stdin.readline()사용
    
- [BOJ 10814](../master/python/10814.py)    

    2차원 배열 정렬, lambda는 쓰고 버리는 일시적인 함수로 필요한 곳에서 즉시 사용하고 버릴 수 있음

#### 21.04.21

- [BOJ 4153](../master/python/4153.py)    

    직각삼각형 문제, while문안에 조건문들을 넣어 계산함 입력받는 순서를 생각하지 못해서 틀렸다 ㅠ
    
#### 21.04.23

- [BOJ 1978](../master/python/1978.py)    
    
    소수 찾는 문제, 1과 자기 자신으로만 나누어지는지 if문과 for문으로 계산함
    
- [BOJ 1259](../master/python/1259.py)      

    팰린드롬수, 리스트 슬라이싱 [시작인덱스 : 종료인덱스 : 진행값] 을 이용해 진행값에 -1을 써 거꾸로 진행되도록 함
    문자열도 가능함
    
  