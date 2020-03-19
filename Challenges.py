# Sort
## 1
def solution(array, commands):

    answer = []
    temp = 0
    
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1:commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2] - 1])
    
    return answer




# Heap
## 1
def unequal(x):
        return x >= K

def solution(scoville, K):
       
    count = 0
    
    for _ in range(len(scoville) - 1):
        if False in list(map(unequal, scoville)):
            scoville.append(scoville[0] + (scoville[1] * 2))
            scoville.remove(scoville[0])
            scoville.remove(scoville[0])
            scoville.sort()
            count += 1
    
    if False in list(map(unequal, scoville)):
        return -1
    else:
        return count
