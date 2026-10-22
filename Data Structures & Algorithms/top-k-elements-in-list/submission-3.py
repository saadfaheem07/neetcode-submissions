class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        frequency = [[] for i in range(len(nums) + 1)]

        for num, count in freq.items():
            frequency[count].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res
