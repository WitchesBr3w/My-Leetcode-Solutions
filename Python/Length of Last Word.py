#For problem number 58 on leetcode.
#Link: https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        return len(a[-1])
