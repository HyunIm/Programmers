# File : 12901.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-25
# Brief : 연습 문제

def solution(a, b):
    d = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    w = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = w[(sum(d[:a-1]) + b) % 7]
    return day
