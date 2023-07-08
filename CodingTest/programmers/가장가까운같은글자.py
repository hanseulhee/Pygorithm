def solution(s):
    answer = []
    d = dict()

    for i in range(len(s)):
        if s[i] in d:
            answer.append(i - d[s[i]])
            d[s[i]] = i
        else:
            d[s[i]] = i
            answer.append(-1)
    return answer