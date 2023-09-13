def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    for i, j in enumerate(score):
        if i%m == m-1:
            answer += j * m
    return answer
