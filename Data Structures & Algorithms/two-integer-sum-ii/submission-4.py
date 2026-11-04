class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sumPair = numbers[left] + numbers[right]

            if sumPair == target:
                return [left + 1, right + 1]
            elif sumPair < target:
                left += 1
            else:
                right -= 1