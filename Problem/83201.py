# File : 823201.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-11
# Brief : 위클리 챌린지

def solution(scores):
    grade = []
    length = len(scores)
    answer = ''

    for i in range(length):
        s = 0
        s_max = 0
        s_min = 100

        for j in range(length):
            s += scores[j][i]
            s_max = s_max if s_max >= scores[j][i] else scores[j][i]
            s_min = s_min if s_min <= scores[j][i] else scores[j][i]

        if s_max == scores[i][i]:
            f = 0
            for j in range(length):
                if scores[j][i] == s_max:
                    f += 1
            if f == 1:
                s -= scores[i][i]
                s //= (length - 1)
            else: s //= length

        elif s_min == scores[i][i]:
            f = 0
            for j in range(length):
                if scores[j][i] == s_min:
                    f += 1
            if f == 1:
                s -= scores[i][i]
                s //= (length - 1)
            else: s //= length

        else: s //= length
        grade.append(s)

    for i in grade:
        answer = answer + 'FFFFFDDCBAA'[i // 10]

    return answer
