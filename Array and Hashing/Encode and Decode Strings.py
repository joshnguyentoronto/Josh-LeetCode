'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode


Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
    One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
    One possible encode method is: "we:;say:;:::;yes"
'''

# Join many string into 1 string is easy, but not when you want to divide it into original array cause we don't know where to split them
# So we can use any random character like @ to easily detect it to decode
# but what if the string have character @ and we decode wrong!
# So then we can use a number along with special character like @ to recognize and decode correctly
class Solution:
    def encode(strs):
        res = ''
        for string in strs:
            res = res + str(len(string)) + '@' + string
        return res

    def decode(str):
        res = []
        i = 0
        while i < len(str):
            length = int(str[i])
            if str[i+1] == '@':
                res.append(str[ i+2 : i+2+length])
            i += 2 + length
        return res


res = Solution.encode(["I","love","you","a", "lot"])
print(res)
print(Solution.decode(res))