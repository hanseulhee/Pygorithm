## 코딩 테스트 준비

#### 22.06.07

- [BOJ 2557](./python/2557.py)

Hello World!를 출력하는 문제

- [BOJ 9498](./python/9498.py)

if ~ else 문제, 파이썬은 if, elif, else로 이루어져있다.

사용자가 값을 입력할 때에

```python
input()
```

은 모든 것을 <b>문자열</b>로 취급한다.

따라서 자료형을 변경할 수 있다.

```python
int(input()) # 정수형
float(input()) # 실수형
```

- [BOJ 2739](./python/2739.py)

구구단 문제, for문을 이용하여 풀었고 print 괄호 안의 출력할 값들을 쉼표로 구분하였다.

```python
range(1, 10) # 1부터 9까지
```

range 함수는 시작 값 이상 종료 값 미만이다.

#### 22.06.08

- [BOJ 2741](./python/2741.py)

N찍기 문제, range 함수를 이용하여 1부터 N까지 출력하였다.

- [BOJ 2588](./python/2588.py)

세자리 수 곱셈 문제, 두번째 수는 하나하나 쪼개서 곱하기 때문에 문자열로 받아야만 쪼갤 수 있어 input()으로 받았다.

```python
print(list(y)) # ['1', '2', '3']
```

list()를 사용하여 입력 값을 리스트로 변경해주고 뒷자리부터 곱해야하므로 이를 뒤집어 주었다.

<b>reverse VS reversed</b>

reverse는 list타입에서 제공하는 함수로 아래와 같은 형태를 가진다.

```python
list.reverse()
```

reversed는 내장 함수다.

```python
reversed(var)
```

- [BOJ 1330](./python/1330.py)

두 수 비교하는 문제, input().split()로 값을 여러 개 입력받고 정수형으로 변환하기 위해 map을 사용하였다.

#### 22.06.09

- [BOJ 2753](./python/2753.py)

윤년 문제, and 연산자와 or 연산자를 통해 풀 수 있었다.

- [BOJ 10871](./python/10871.py)

X보다 작은 수 문제, N개의 수열 A이므로 N까지의 i를 돌며 만약 A[i]가 X보다 작으면 해당 값을 출력하였다.

- [BOJ 14681](./python/14681.py)

사분면 고르기 문제, if문으로 나열하여 풀었다. 이게 최선일까?

#### 22.06.10

- [BOJ 2920](./python/2920.py)

음계 문제, 오름차순과 내림차순을 이용하여 풀었다.

<b>sort VS sorted</b>

sort 함수는 리스트 형의 메소드이며 리스트 원본 값을 직접 수정한다. (None을 반환한다)

```python
list.sort()
```

sorted 함수는 내장함수로 리스트 원본 값은 그대로이며 정렬한 값을 반환한다.

```python
sorted(list)
```

따라서 list를 <b>변경하려면 list.sort()</b>를 사용하고 <b>새로운 정렬된 객체가 필요하면 sorted()</b>를 사용하면 된다.

- [BOJ 1978](./python/1978.py)

소수 찾는 문제, 1은 소수가 아니므로 예외처리하였다.

- [BOJ 10828](./python/10828.py)

스택 문제, input()을 사용하면 시간초과가 나기 때문에
<b>sys.stdin.readline()</b>을 사용하였다.

<b>sys.stdin.readline()</b>은 문자열로 받아지고, 한 줄 단위로 입력을 받기 때문에 리스트와 같이 여러 개의 값을 입력받아야 할 경우에는 split() 함수로 공백을 기준으로 값을 나눌 수 있다.

<b>입출력 속도</b>

sys.stdin.readline > raw_input > input
