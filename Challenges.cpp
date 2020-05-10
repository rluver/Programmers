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
