# File : 12903.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-25
# Brief : 연습 문제

def solution(s):
    l = len(s)
    return s[l//2] if l%2 else s[l//2-1:l//2+1]
