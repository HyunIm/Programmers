# File : 12906.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-25
# Brief : 연습 문제

def solution(arr):
    a = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            a.append(arr[i])
    return a
