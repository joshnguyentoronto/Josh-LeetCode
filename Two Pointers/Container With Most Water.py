'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
'''

# Time limit exceed solution:
# class Solution:
#     def maxArea( height):
#         area = 0
#         for i in range(len(height)):
#             j = i+1
#             while j < len(height):
#                 area = max(  area, (j-i) * min(height[i], height[j])  )
#                 j += 1
#         return area

# New Solution:
class Solution:
    def maxArea( height):
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = max(  area, (r-l) * min( height[l], height[r] )  )
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            elif height[l] == height[r] and height[l+1] > height[r-1]:
                r -= 1
            elif height[l] == height[r] and height[l+1] < height[r-1]:
                l -= 1
        return area

print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))