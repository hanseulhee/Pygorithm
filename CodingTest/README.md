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
