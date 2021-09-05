# File : 82612.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-05
# Brief : 위클리 챌린지

def solution(price, money, count):
    for i in range(1, count+1):
        money -= price * i
    return 0 if money > 0 else -money
