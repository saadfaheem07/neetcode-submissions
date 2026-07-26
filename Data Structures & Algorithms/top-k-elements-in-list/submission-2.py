class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        arr = []
        for key,value in d.items():
            arr.append([value,key])
        arr.sort()
        print(arr)
        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res