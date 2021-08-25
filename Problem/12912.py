# File : 12912.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-25
# Brief : 연습 문제

def solution(a, b):
    a = [a, b]
    r = [i for i in range(min(a), max(a)+1)]
    return sum(r)
