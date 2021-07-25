# File : 42891.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-25
# Brief : 그리디

def solution(food_times, k):
    answer = 0
    n = len(food_times)

    for _ in range(k):
        while food_times[answer] == 0:
            if sum(food_times)==0: break
            answer += 1
            if answer >= n: answer = 0

        food_times[answer] -= 1
        answer += 1
        if answer >= n: answer = 0

    answer += 1
    return answer
