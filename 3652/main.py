import numpy as np

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original = sum(a * b for a, b in zip(prices, strategy))
        maximum = original
        half=int(k/2)
        profit1 = sum(prices[half:k])+sum(a * b for a, b in zip(prices[k:], strategy[k:]))
        if profit1>maximum:
            maximum=profit1
        for i in range(1,len(prices)):
            if i+k<=len(prices):
                profit=profit1+(prices[i-1]*strategy[i-1])-(prices[i+half-1])-(prices[i+k-1]*strategy[i+k-1])+prices[i+k-1]
                if profit>maximum:
                    maximum=profit
                profit1=profit

        return maximum
        
