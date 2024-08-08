from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0, nums
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        print(nums)
        print(k)
        nums[k: len(nums)] = [None] * (len(nums) - k)
        print(nums)
        return k

nums = [1,1,2]  # [1,2,_]


nums = [0,0,1,1,1,2,2,3,3,4]  # [0,1,2,3,4]
print(Solution().removeDuplicates(nums))



