'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that 
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

# Runtime beats 5%
# Memory beats 95%
class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        if len(temperatures) > 20:
            tem = set(temperatures)
            highest = max(tem)
            for i in range(len(temperatures)):
                if i == len(temperatures) - 1:
                    return answer
                elif temperatures[i] == highest:
                    answer[i] = 0
                elif temperatures[i] == temperatures[i-1] and i != 0:
                    if answer[i-1] == 0:
                        answer[i] = 0
                    else:
                        answer[i] = answer[i-1] - 1
                else:
                    day = 0
                    for j in range(i+1, len(temperatures)):
                        if temperatures[j] > temperatures[i]:
                            answer[i] = day + 1
                            break
                        elif temperatures[j] <= temperatures[i]:
                            day += 1
            return answer
        else:
            for i in range(len(temperatures)):
                if i == len(temperatures) - 1:
                    return answer
                day = 0
                for j in range(i+1, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        answer[i] = day + 1
                        break
                    elif temperatures[j] <= temperatures[i]:
                        day += 1


# Runtime beats:76%
# Memory beats: 13.86%
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = [] # store a pair [idx, tem]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx, tem = stack.pop()
                answer[idx] = i - idx
            stack.append([i, t])
        return answer
'''