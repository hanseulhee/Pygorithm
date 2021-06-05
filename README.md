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
    
#### 21.04.24

- [BOJ 2798](../master/python/2798.py) 

    블랙잭 문제, 삼중 for문 돌림  
    
- [BOJ 11050](../master/python/11050.py) 

    이항계수 문제, math 모듈의 factorial함수 사용 
    [팩토리얼](https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python)
 
#### 21.04.25

- [BOJ 1920](../master/python/1920.py) 

    시간초과, 출력초과 자꾸남 ㅠ Set 함수를 이용해 요소들의 포함 여부를 확인, 삼항연산자 사용
    
    [시간복잡도](https://chancoding.tistory.com/43) [이진탐색/이분탐색](https://velog.io/@yeseolee/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Binary-Search%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89) [삼항연산자](https://ooyoung.tistory.com/116)

#### 21.04.26

- [BOJ 11051](../master/python/11051.py)     

    이항계수 구하는 문제   
    
#### 21.04.27

- [BOJ 11401](../master/python/11401.py)

    페르마의 소정리, 큰 수가 들어왔을 때 시간초과가 나서 페르마의 소정리를 이용함 어렵당당
    [페르마의 소정리](https://www.acmicpc.net/board/view/15795)

#### 21.05.09

- [BOJ 1157](../master/python/1157.py)     

    대소문자 구분없이 비교하는 문제, 소문자로 변경 lower(), 대문자로 변경 upper() 
    if문으로 max값이 두개 이상인 경우 '?'을 출력하도록 함     
    
- [BOJ 1546](../master/python/1546.py)

    공식에 맞게 바꾸어 평균 값 구하는 문제, 빈 리스트에 append() 안해서 오류났지만 해결 ~~~
    
- [BOJ 2164](../master/python/2164.py)

    덱 사용, 덱은 가장자리에 원소를 넣거나 뺄 수 있어 popleft() 사용 
    [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)  [Queue](https://yunaaaas.tistory.com/29)
  
- [BOJ 2475](../master/python/2475.py)
    
    검증수 문제, for문으로 리스트 값 각각의 제곱 값 구함
         
#### 21.05.10

- [BOJ 2908](../master/python/2908.py)

    두 개의 숫자를 역순으로 바꾸어 더 큰 숫자 출력, [::-1] 연산자 이용
    
#### 21.05.14

- [BOJ 10809](../master/python/10809.py)

    아스키코드의 숫자 범위로 리스트 생성, chr함수로 아스키코드에 맞는 문자열로 변환시킴, find함수는 문자열에서만 사용 가능

#### 21.05.15

- [BOJ 1085](../master/python/1085.py)

    4개의 거리중에 가장 짧은 거리를 min 함수를 통해 구했음
    
 - [BOJ 2231](../master/python/2231.py)   
 
    브루트 포스 문제, for문으로 1부터 m까지 분해합 구해서 계산했지만 어렵다 ... 
    
#### 21.05.18

- [BOJ 2884](../master/python/2884.py)

    알람시계 문제, if문으로 조건에 맞게 45분을 일찍 할 수 있었음    
    
#### 21.05.19

- [BOJ 1110](../master/python/1110.py)

    더하기 싸이클 문제, while문 사용. //10 으로 십의 자리를 구하고 %10 으로 일의 자리를 구함 count 변수 만들어서 사이클의 길이를 구함!    

#### 21.05.24

- [BOJ 10250](../master/python/10250.py)

    ACM 호텔 문제, 각 조건들을 어떻게 계산해야할지 생각하는게 힘들었다. for문을 이용해 계산하고 if문으로 예외처리도 해줬다.
    
#### 21.05.26

   코드리뷰 피드백 받고 고치기! 
   
   배운 점 
   - range 메소드는 list 객체를 반환한다는 점
   - sys.stdin.readlines: 모든 줄을 다 읽음, sys.stdin.readline: 한 줄만 읽음
   
#### 21.06.05

- [BOJ 2750](../master/python/2750.py)

    수 정렬하기 문제, sorted 써서 오름차순 정렬함
    
#### 21.06.06

- [BOJ 1924](../master/python/1924.py)

    calendar 모듈 사용, calendar 모듈의 weekday 메소드는 년도, 월, 일을 매개변수로 받아서 요일 정보를 리턴함

    