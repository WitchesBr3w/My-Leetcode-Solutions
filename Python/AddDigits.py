class Solution():
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
            
        while num > 10:
            result = 0
            string = str(num)
            
            for x in range(0,len(string)):
                integer = int(string[x])
                result = result + integer
            num = result
        
        return num
