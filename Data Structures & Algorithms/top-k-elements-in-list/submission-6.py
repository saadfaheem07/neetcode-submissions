class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = defaultdict(int)
        for i in nums:
            buckets[i] += 1
        
        freq = [[] for _ in range(len(nums) + 1)] #index denotes frequency here, and the cell is the actual list of elements with 'index' number of times they occur in the array

        for num, count in buckets.items():
            freq[count].append(num)
        
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
