#For problem number 67 on leetcode.
#Link: https://leetcode.com/problems/add-binary/

class Solution:
    def binary_to_decimal(self, binary)
        decimal = 0
        power = 0
        
        for digit in reversed(binary):
            if digit == '1':
                decimal += 2 ** power
            power += 1
            
        return decimal

    def decimal_to_binary(self, num) 
        if num == 0:
            return "0"
        
        result = ""
        while num > 0:
            result = str(num % 2) + result
            num //= 2
            
        return result

    def addBinary(self,a,b)
        dec_a = self.binary_to_decimal(a)
        dec_b = self.binary_to_decimal(b)
        
        total = dec_a + dec_b
        
        return self.decimal_to_binary(total)
