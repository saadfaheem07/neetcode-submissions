class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 0
        
        for i in nums:
            d[i] += 1
        
        d = sorted(d,key = d.get,reverse=True)
        l = []
        for i in range(k):
            l.append(d[i])
        
        return l