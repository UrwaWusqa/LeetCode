class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        max_area = -1
        hrem=set()
        hfp=[1]+hFences+[m]
        vfp =[1]+vFences+[n]
        for i,h in enumerate(hfp):
            for h_ in hfp[i+1:]:
                diff = abs(h_-h)
                hrem.add(diff)

        for i,h in enumerate(vfp):
            for h_ in vfp[i+1:]:
                diff = abs(h_-h)
                if diff in hrem:
                    max_area=max(max_area,diff*diff)

        if max_area==-1:
            return max_area
        else:
            return max_area%1000000007
