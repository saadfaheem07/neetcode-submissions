class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for num in nums:
            if num == 0:
                i += 1
        
        if i > 1:
            return [0] * n
        
        totalProduct = 1
        for j in nums:
            if j != 0:
                totalProduct *= j
        
        if i == 1:
            l = [0] * n
            for j in nums:
                if j == 0:
                    index = nums.index(j)
                    l[index] = totalProduct
        
            return l
        
        l = []
        for j in nums:
            l.append(totalProduct // j)
        
        return l