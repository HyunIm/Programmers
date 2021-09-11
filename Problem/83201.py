# File : 83201.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-11
# Brief : 위클리 챌린지

def solution(scores):
    grade = []
    length = len(scores)
    a = list(map(list, zip(*scores)))
    answer = ''

    for i, j in enumerate(a):
        s = sum(j)
        if (max(j) == a[i][i] and j.count(max(j)) == 1) or (min(j) == a[i][i] and j.count(min(j)) == 1):
            s -= a[i][i]
            s //= (length - 1)
        else:
            s //= length
        grade.append(s)

    for i in grade:
        answer = answer + 'FFFFFDDCBAA'[i // 10]

    return answer
