# File : 12928.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-25
# Brief : 연습 문제

def solution(n):
    r = n
    for i in range(1, n):
        if n%i==0: r += i
    return r
