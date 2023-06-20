# 기록

<details>
<summary>입력</summary>
<div>

input은 입력된 값을 **문자열**로 인식해준다.

입력된 값을 정수형으로 바꾸고 싶다 **int** 함수를 이용한다.

```python
a = int(input("입력: "))
```

입력값을 두 개 이상으로 구분할 때 **split** 함수를 이용한다.

```python
a = input("입력: ").split()
```

그러나 int 함수는 리스트를 정수형으로 바꾸지 못한다. 이 때 map 함수를 사용한다.

```python
a = map(int, input("입력: ").split())
```

</div>
</details>

<details>
<summary>줄바꿈, 공백</summary>
<div>

**줄바꿈**

파이썬에서 줄바꿈 **\n**

줄바꿈 없이 출력하고 싶다면

```python
print("Hello", end=" ")
print("World")
```

---

**공백**

**strip** 함수는 문자열 내에서 원하는 문자열 또는 공백을 모두 제거한다.

```python
string = "    seulhee   "
print(string.strip())

# "seulhee"
```

</div>
</details>

<details>
<summary>대소문자</summary>
<div>

**대문자**

```python
str.upper()
```

**소문자**

```python
str.lower()
```

**대문자 있는지 확인**

```python
str.isupper()
```

**대소문자 상호 전환**

```python
str.swapcase()
```

</div>
</details>

<details>
<summary>for문</summary>
<div>

데이터의 길이만큼 반복

```python
len(변수명)
```

</div>
</details>

<details>
<summary>삼항연산자</summary>
<div>

```python
[값1] if [조건문] else [값2]
```

</div>
</details>

<details>
<summary>연산자</summary>
<div>

**나누기 연산자**

몫
//

나머지
%

**or 연산자**

파이썬에서 or 연산자는 **or**

```python
if (a == b or c == a):
```

</div>
</details>

<details>
<summary>리스트</summary>
<div>

비어있는 리스트

```python
empty = list()
```

</div>
</details>
