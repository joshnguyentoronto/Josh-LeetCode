'''
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. 
Tasks could be done in any order. 
Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that 
represents the cooldown period between two same tasks 
(the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
    A -> B -> idle -> A -> B -> idle -> A -> B
    There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
    ["A","A","A","B","B","B"]
    ["A","B","A","B","A","B"]
    ["B","B","B","A","A","A"]
    ...
    And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
    One possible solution is
    A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
'''

import heapq

# My solution
# Quite inefficient
# Run 5%, Space 60%
class Solution:
    def leastInterval(tasks, n):
        if n == 0:
            return len(tasks)
        res = 0
        taskMap = {}
        unitMap = {}
        # O(n)
        for task in tasks:
            if task in taskMap:
                taskMap[task] += 1
            else:
                taskMap[task] = 1
        # O(26)
        for task in taskMap:
            unitMap[task] = 0
        # O(n)
        while taskMap:
            # O(26)
            arr = [k for k,v in unitMap.items() if v == 0]
            if arr:
                curTask = 'A'
                curmax = 0
                # O(26)
                for task in arr:
                    if taskMap[task] > curmax:
                        curmax = taskMap[task]
                        curTask = task
                res += 1
                taskMap[curTask] -= 1
                # O(26)
                for task in unitMap:
                    if unitMap[task] > 0:
                        unitMap[task] -= 1
                unitMap[curTask] = n
                if taskMap[curTask] == 0:
                    del taskMap[curTask]
                    del unitMap[curTask]
            else:
                res += 1
                # O(26)
                for task in unitMap:
                    unitMap[task] -= 1
        return res

#  A bit more efficient
# Run 5%, Space 87.75%
    def leastInterval2(tasks, n):
        if n == 0:
            return len(tasks)
        res = 0
        taskMap = {}
        # O(n)
        for task in tasks:
            if task in taskMap:
                taskMap[task][0] += 1
            else:
                taskMap[task] = [1, 0]
        # O(n)
        while taskMap:
            m = -1
            t = 'a'
            # O(26)
            for task in taskMap:
                if taskMap[task][1] == 0 and taskMap[task][0] > m:
                    m = taskMap[task][0]
                    t = task
            if t == 'a':
                res += 1
                # O(26)
                for task in taskMap:
                    taskMap[task][1] -= 1
            else:
                res += 1
                # O(26)
                for task in taskMap:
                    if taskMap[task][1] > 0:
                        taskMap[task][1] -= 1
                if m == 1:
                    del taskMap[t]
                else:
                    taskMap[t] = [m - 1, n]
        return res


print(Solution.leastInterval2(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))