# def solution(n):
#     answer = 0
#     for i in range(n):
#         if n == 1:
#             return 0
#         if i % 2 == 0:
#             answer += i
    
#     if n % 2 == 0:
#         answer += n
#     return answer

def solution(n):
    answer = 0
    for i in range(0, n+1):
        if i % 2 == 0: answer += i

    return answer
