# Hash
## 1
'''fail to satisfy efficiency'''
def solution(participant, completion):
    
    if len(participant) > 1:
        for i in completion:
            participant.remove(i)
    
    answer = participant[0]
    
    return answer

---------------------------------------------------------------

from collections import Counter

def solution(participant, completion):
    
    if len(participant) > 1:
        cnt1 = Counter([x for x in participant])
        cnt2 = Counter([x for x in completion])
        answer = list(cnt1 - cnt2)[0]
    
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




# Stack/Queue
## 1
def solution(heights):
    
    answer = [0]    
    
    for i in range(1, len(heights)):
        index = 0
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                index = j + 1
                break
        answer.append(index)
        
    return answer


# 3
from collections import Counter

def solution(progresses, speeds):
    
    diff = list(map(lambda x, y: (100 - x) / y, progresses, speeds))
    time = list(map(lambda x: int(x) if x - int(x) == 0.0 else int(x) + 1, diff))
    
    for i in range(len(time) - 1):
        if time[i] > time[i + 1]:
            time[i + 1] = time[i]
    
    count = Counter(time)
    answer = list(count.values())
    
    return answer




# Heap
## 1  
'''fail to satisfy efficiency'''
def solution(scoville, K):
    
    cnt = 0
    scoville.sort()
    
    if len(scoville) == 0:
        return -1
    elif K == 0:
        return cnt
    if len(scoville) <= 1:
        if scoville[0] >= K:
            return cnt
        else:
            return -1
    else:
        while scoville[0] < K:
            cnt += 1
            scoville.append(scoville[0] + 2 * scoville[1])
            scoville.pop(0)
            scoville.pop(0)
            scoville.sort()            
            if len(scoville) == 1 and scoville[0] < K:
                return -1
            
    return cnt


import heapq

def solution(scoville, K):
    
    cnt = 0
    heapq.heapify(scoville)
    
    if len(scoville) == 0:
        return -1
    elif K == 0:
        return cnt
    if len(scoville) <= 1:
        if scoville[0] >= K:
            return cnt
        else:
            return -1
    else:
        while scoville[0] < K:
            cnt += 1
            min0 = heapq.heappop(scoville)
            min1 = heapq.heappop(scoville)
            heapq.heappush(scoville, min0 + 2 * min1)            
            if len(scoville) == 1 and scoville[0] < K:
                return -1
            
    return cnt

    
    
    
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


## 2
import math
from itertools import permutations
   
def solutions(numbers):
    
    length = len(numbers)
    permutation = []
    
    for i in range(length):
        temp = permutations(numbers, i + 1)
        permutation.append([''.join(i) for i in temp])
        
    permutation = sum(permutation, [])
    permutation = list(set(permutation))
        
    permutation = list(filter(lambda x: int(x) / 2 == 1.0 or int(x[-1]) % 2 != 0, permutation))
    permutation = list(filter(lambda x: int(x) / 3 == 1.0 or sum([int(i) for i in x]) % 3 != 0, permutation))
    permutation = list(filter(lambda x: int(x) / 5 == 1.0 or int(x[-1]) % 5 != 0, permutation))    
    
    permutation = list(map(lambda x: int(x), permutation))
        
    permutation = list(set(permutation))
    permutation.sort()
    
    if 0 in permutation:
        permutation.remove(0)
    if 1 in permutation:
        permutation.remove(1)
    
         
    for i in permutation:
        if(i >= 10):
            for j in range(2, int(math.sqrt(i))):
                if(i % j == 0):
                    permutation.remove(i)
                    break
                           
    answer = len(permutation)
    
    return(answer)
