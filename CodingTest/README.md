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

#### 22.06.11

- [BOJ 11721](./python/11721.py)

문자열 끊어서 출력하는 문제, <b>range(start, end, step)</b>를 이용해 10개씩 끊었다. <b>a[start:원하는 종료값 + 1]</b>로 작성하여 처음에 0부터 9까지 끊어지면 다음번엔 10부터 19까지 끊어지도록 하였다.

#### 22.06.13

- [BOJ 10845](./python/10845.py)

큐 문제, append는 새로운 요소를 배열 맨 끝에 추가한다. insert는

```python
array.insert(i, x)
```

이와 같은 형태로 원하는 위치 i 앞에 x라는 값을 삽입한다.

큐는 FIFO(First-In-First-Out) 선입선출 구조이기 때문에 insert를 사용하였다.

<b>stack VS queue</b>

stack은 삽입과 삭제가 한 쪽에서 일어나지만 queue는 삽입과 삭제가 다른 쪽에서 일어난다.

#### 22.06.14

- [BOJ 10866](./python/10866.py)

덱 문제, 덱은 양쪽에서 모두 입출력이 가능하여 스택과 큐에 비해 자유도가 높다.

#### 22.06.18

- [BOJ 10816](./python/10816.py)

숫자 카드 2 문제,

```python
count = {}

for i in numCard:
    if(i in count):
        count[i] += 1
    else:
        count[i] = 1

for j in countCard:
    if j in count:
        print(count[j], end=" ") # 존재하는 숫자라면
    else:
        print(0, end=" ") # 존재하지 않는 숫자라면 0을 출력한다.
```

빈 딕셔너리를 생성하여 데이터를 추가할 수 있도록 하였고 key 값을 찾아 value를 출력하고 key가 countCard에 없는 값이라면 0을 출력하도록 하였다.

- [BOJ 11866](./python/11866.py)

(N, K)-요세푸스 순열을 구하는 문제, 큐로 풀 수 있었다. popleft()함수를 이용하여 K-1 만큼 왼쪽으로 원형을 돌며 값을 출력하였고 사람들이 모두 제거될 때까지 반복하였다.

- [BOJ 1018](./python/1018.py)

체스판 다시 칠하기 문제, 이러한 문제를 <b>브루트포스</b>라 하는데 모든 경우의 수를 탐색함으로써 원하는 결과를 도출하는 문제를 의미한다.

4중 for문을 이용하여 풀었다.

```python
for i in range(N-7):  # 행
    for j in range(M-7):  # 열
        WCount = 0  # W
        BCount = 0  # B
```

8\*8로 맞춰야 하므로 행과 열을 -7로 하여 고정시켰다.

```python
for row in range(i, i+8):
    for column in range(j, j+8):
        if(row + column) % 2 == 0:
            if array[row][column] != "W":
                WCount += 1
            if array[row][column] != "B":
                BCount += 1
        else:
            if array[row][column] != "B":
                WCount += 1
            if array[row][column] != "W":
                BCount += 1
```

행과 열의 합이 짝수라면 시작점의 색깔과 같고, 홀수라면 달라야 해 이를 조건문으로 확인 후 count에 1을 더해주었다.

#### 22.06.19

- [BOJ 2775](./python/2775.py)

부녀회장이 될테야 문제, people이라는 배열에 입력받은 1부터 호수까지의 값을 담았다.
이후 2중 for문으로 층 수 만큼 반복하고 두번째 for문에서 층 수가 증가할 때마다 -1층의 이 전 호실 사는 사람의 수를 더했다.

이후 마지막 수를 출력하여 반환하였다.

- [BOJ 1874](./python/1874.py)

스택 수열 문제, 파이썬에서 push는 append, pop은 pop을 사용한다.

#### 22.06.24

- [BOJ 1874](./python/1874.py)

스택으로 수열만드는 문제, 스택은 가장 나중에 들어간 게 처음에 나오는 구조로 스택에 수를 push 할 때 반드시 오름차순으로 push를 할 수 있다는 점을 생각하며 풀었다.

#### 22.06.25

- [BOJ 10773](./python/10773.py)

입력받은 숫자가 0이라면 pop을 이용해 배열에서 삭제하고 아닐 경우 배열에 입력받은 수를 더한다. 이후 sum을 이용해 배열의 값을 모두 더하여 반환한다.

- [BOJ 1436](./python/1436.py)

666이 들어가 있는 숫자를 찾고 666이 포함되어 있는 수 중에 몇번째 수인지 찾는 문제, 브루트포스 (완전탐색) 문제에서 하나하나 찾을 때엔 while True를 쓰자.

- [BOJ 11651](./python/11651.py)

좌표 정렬하기 2 문제, y를 기준으로 오름차순 정렬이 되야하므로 [y, x] 형태로 배열에 append 하였다.

#### 22.06.27

- [BOJ 1463](./python/1463.py)

전의 결과를 다음 결과에 이용하는 DP문제(다이나믹 프로그래밍), min 함수는 min(iterable1, iterable2)일 경우 iterable1 과 iterable2 중 더 작은걸 반환한다.

- [BOJ 9095](./python/9095.py)

DP문제, i가 3보다 크면 dp[i] = dp[i-1]+dp[i-2]+dp[i-3] 규칙이 있다는 것을 이용해 풀었다.

- [BOJ 11047](./python/11047.py)

얼마를 모으기 위해 필요한 동전 개수의 최솟값을 구하는 문제, 내림차순으로 정렬하여 k가 0이 되면 반환하도록 하였다.

#### 22.06.28

- [BOJ 11399](./python/11399.py)

ATM 문제, 오름차순으로 정렬하는 것이 제일 최소임을 이용해 풀었다. 배열[0:i]는 0부터 i-1번째까지의 요소를 꺼낸다.

- [BOJ 2579](./python/2579.py)

계단의 점수들을 합하여 총 점수의 최댓값을 구하는 문제, DP문제.

```python
dp.append(max(dp[i-2] + array[i], dp[i-3] + array[i] + array[i-1]))
```

3칸 연속으로 올라오는 경우는 없어 올라갈 수 있는 경우 중 더 큰값을 찾아 dp 리스트에 추가하였다.

#### 22.07.03

- [BOJ 2606](./python/2606.py)

웜 바이러스 문제, DFS(깊이 우선 탐색), BFS(너비 우선 탐색)로 해결할 수 있는 문제로 난 DFS로 풀어보았다.

파이썬 def 함수를 언제쓰냐? -> 긴코드를 짧게 축약할 때, 인자를 전달해서 풀이할 때
