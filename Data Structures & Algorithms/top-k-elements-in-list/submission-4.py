class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = defaultdict(int)
        f = [[] for i in range(len(nums) + 1)]

        for i in nums:
            n[i] += 1

        for num, count in n.items():
            f[count].append(num)

        res = []
        for i in range(len(f) - 1, 0, -1):
            for j in f[i]:
                res.append(j)
                if len(res) == k:
                    return res