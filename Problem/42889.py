# File : 42889.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-28
# Brief : 정렬

def solution(n, stages):
    length = len(stages)
    a = []
    for i in range(1, n + 1):
        c = stages.count(i)

        if length == 0:
            r = 0
        else:
            r = c / length

        a.append([i, r])
        length -= c

    a.sort(key=lambda x: -x[1])
    answer = [i[0] for i in a]

    return answer
