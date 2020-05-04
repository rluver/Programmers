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
    
    
## 3
from collections import Counter

def solution(clothes):
    
    answer = 1
    
    cnt = Counter([x[1] for x in clothes])
    for i in cnt.values():
        answer *= (i + 1)
        
    answer -= 1
    
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
def permutation(numbers):
    
    result = [numbers[:]]
    arr = [0] * len(numbers)
    i = 0
    while i < len(arr):
        if arr[i] < i:
            if i % 2 == 0:
                numbers[0], numbers[i] = numbers[i], numbers[0]
        else:
            numbers[arr[i]], numbers[i] = numbers[i], numbers[arr[i]]
        result.append(numbers[:])
        arr[i] += 1
        i = 0
    else:
        arr[i] = 0
        i += 1
        
    return result


def solution(numbers):
    
    numbers = permutation(numbers)
    
    for i in range(len(numbers)):
        numbers[i] = ''.join(list(map(str, numbers[i])))
        
    if int(max(numbers)) == 0:
        return str(0)
    else:
        return max(numbers)




# Brute-Force Search
## 1
def solution(answer):
    
    student = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    
    student_answer = [[], [], []]
   
    for i in range(0, 3):
        quotient, remainder = divmod(len(answer), len(student[i]))
        student_answer[i] = student[i] * quotient + student[i][ : remainder]
        
        
    result = [[], [], []]
    
    for i in range(0, 3):        
        result[i] = [i + 1, sum(list(map(lambda j: student_answer[i][j] == answer[j], range(len(answer)))))]
        
    
    sum_max = max(map(lambda x: x[:][1], result))    
    answer = []

    for i in range(len(result)):
        if result[i][1] == sum_max:
            answer.append(i + 1)
   
    
    return(answer)
