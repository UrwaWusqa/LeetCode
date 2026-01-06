import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors={}
        result=0
        for num in nums:
            divi = []
            for i in range(1,int(sqrt(num)+1)):
                if num%i==0:
                    divi.append(i)
            print(num,divi)
            if len(divi)==2:
                if sqrt(num) not in divi:
                    for i in divi:
                        result=result+i+int(num/i)
        return result
