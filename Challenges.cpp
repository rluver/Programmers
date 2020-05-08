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
