# Q7 Answer Template

def solution(arr):
    answer = []
    
    for a in arr:
        if(a not in answer):
            answer.append(a)

    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)
