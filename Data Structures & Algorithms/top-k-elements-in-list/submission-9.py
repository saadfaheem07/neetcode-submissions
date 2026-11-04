class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in d.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res