'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''


class Solution:
    def groupAnagrams(self, strs):
        if len(strs) <= 1:
            return [strs]
        # using dict to store sorted anagram and its original word 
        diction = {}
        for string in strs:
            # convert string to set -> sort that set -> join again into string
            s = ''.join(sorted(string))
            if s not in diction:
                diction[s] = [string]
            elif s in diction:
                diction[s].append(string)
        return diction.values()