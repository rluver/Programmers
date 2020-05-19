# Hash
## 1

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) 
{
    int i;
    string answer = "";

    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for (i = 0; i < participant.size(); i++)
    {
        if (i <= participant.size() - 2)
        {
            if (participant[i] != completion[i])
            {
                answer = participant[i];
                break;
            }
        }
        else
        {
            answer = participant[i];
        }
    }

    return answer;
}




# Stack/Queue
## 1

vector<int> solution(vector<int> heights)
{
    int i, j, index;
    vector<int> answer(1);

    for (i = 1; i < (int)heights.size(); i++)
    {
        index = 0;
        for (j = i - 1; j >= 0; j--)
        {
            if (heights[i] < heights[j])
            {
                index = j + 1;
                break;
            }
        }
        answer.push_back(index);
    }

    return answer;
}


## 3

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
    double epsilon = 1e-10;
    int i, cnt;
    vector<int> time, answer;
    vector<double> diff;

    for (i = 0; i < (int)progresses.size(); i++)
    {
        diff.push_back((double)(100 - progresses[i]) / (double)speeds[i]);
    }
        
    for (i = 0; i < (int)diff.size(); i++)
    {
        if (diff[i] - (int)diff[i] < epsilon)
        {
            time.push_back(int(diff[i]));
        }
        else
        {
            time.push_back(int(diff[i] + 1));
        }
    }
   
    for (i = 0; i < (int)time.size() - 1; i++)
    {
        if (time[i] > time[i + 1])
        {
            time[i + 1] = time[i];
        }
    }
        
    cnt = 1;
    for (i = 0; i < (int)time.size(); i++)
    {
        if (i < (int)time.size() - 1) 
        {
            if (time[i] == time[i + 1])
            {
                cnt++;
            }
            else
            {
                answer.push_back(cnt);
                cnt = 1;
            }
        }
        else
        {
            if (time[i] == time[i - 1])
            {
                answer.push_back(cnt);
            }
            else
            {
                answer.push_back(1);
            }
        }
    }

    return answer;    
}




# Heap
## 1

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int cnt = 0, i, min0, min1;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (i = 0; i < (int)scoville.size(); i++) 
    {
        pq.push(scoville[i]);
    }
    
    if (pq.size() == 0)
    {
        return -1;
    }
    else if (K == 0)
    {
        return cnt;
    }
    if (pq.size() <= 1)
    {
        if (pq.top() >= K)
        {
            return cnt;
        }
        else
        {
            return -1;
        }
    }
    else
    {
        while (pq.top() < K)
        {
            cnt++;
            min0 = pq.top();
            pq.pop();
            min1 = pq.top();
            pq.pop();
            pq.push(min0 + 2 * min1);
            if (pq.size() == 1 && pq.top() < K)
            {
                return -1;
            }
        }
    }

    return cnt;
}


## 2

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k)
{
    int i, answer = 0, idx = 0;
    priority_queue<int, vector<int>, less<int>> pq;
    
    while (stock < k)
    {
        for (i = idx; i < (int)dates.size(); i++)
        {
            if (stock < dates[i])
            {
                break;
            }
            pq.push(supplies[i]);
            idx = i + 1;
        }
        
        stock += pq.top();
        pq.pop();
        answer += 1;
    }
    
    return answer;    
}
