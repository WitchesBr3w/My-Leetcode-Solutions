#Solution to problem number 191 on leetcode
#Link: https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        if not (1 <= n <= (2**31 - 1)):
            raise ValueError("n must be in range 1 <= n <= 2^31 - 1")

        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
  
