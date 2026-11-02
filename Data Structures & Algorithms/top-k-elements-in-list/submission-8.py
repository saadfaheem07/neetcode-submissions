class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        frequency = [[] for _ in range(len(nums) + 1)] # nums + 1 because we don't need to store in index 0
        for num, count in d.items():
            frequency[count].append(num)
        
        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res