# Hash
## 1
def solution(participant, completion):
    
    if len(participant) > 1:
        for i in completion:
            participant.remove(i)
    
    answer = participant[0]
    
    return answer


## 2
def solution(phone_book):
    
    phone_book.sort(key = lambda x : len(x))
    
    i = 0
    while(i < len(phone_book)):
        test_phone_book = phone_book
        test = phone_book[i]
        test_length = len(test)
        test_phone_book.remove(test)
        condition = test in list(map(lambda x : x[:test_length], test_phone_book))
        
        if condition == True:
            break;
        else:
            i += 1
    
    if condition == True:
        return False
    else:
        return True





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


## 2
def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort()
    numbers = numbers[::-1]
        
    answer = ''.join([i for i in numbers])
         
    if(answer[0] == '0'):
        answer = str(0)
    
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
