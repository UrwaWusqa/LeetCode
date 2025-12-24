from bisect import bisect_left
class Solution:     
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = sorted(events,key=lambda item: item[0])
        n=len(events)
        max_sum=[]
        max_=0
        for event in reversed(events):
            if event[2] > max_:
                max_=event[2]
            max_sum.append(max_)
        max_sum = list(reversed(max_sum))
        starts=[e[0] for e in events]
        
        result=0
        for i, (s,e,v) in enumerate(events):
            bis = bisect_left(starts,e+1)
            if bis<n:
                mx2=max_sum[bis]
            else:
                mx2=0

            result=max(result,v+mx2)
            
        return result
