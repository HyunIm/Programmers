def solution(arr):
    temp = []
    answer = 0

    while True:
        for i in arr:
            if i >= 50 and i%2 == 0:
                temp.append(i//2)
            elif i < 50 and i%2:
                temp.append(i*2 + 1)
            else:
                temp.append(i)
        if arr == temp:
            break
        else:
            arr = temp
            temp = []
            answer += 1

    return answer
