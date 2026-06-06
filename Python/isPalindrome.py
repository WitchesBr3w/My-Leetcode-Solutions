#My first solution involved chaining .replace() and .replace() over and over again but then I realized that it would be too inefficient
# For problem number 125 on leetcode.
# Link: https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        x = "".join(filter(str.isalpha, s.lower()))
        return x == x[::-1]
