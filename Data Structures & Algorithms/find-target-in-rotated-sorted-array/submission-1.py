class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # 1. Found it
            if nums[mid] == target:
                return mid

            # 2. Left half is sorted
            if nums[left] <= nums[mid]:
                # Is target inside the left sorted half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # 3. Right half is sorted
            else:
                # Is target inside the right sorted half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Not found
        return -1