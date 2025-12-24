class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples=sum(apple)
        
        capacity = sorted(capacity)
        count = 0
        for cap in reversed(capacity):
            total_apples=total_apples-cap
            count+=1
            if total_apples<=0:
                return count
