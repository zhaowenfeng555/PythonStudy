class Solution:
    def process(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            print (' '.join(['in', str(left), str(mid), str(right)]))

        print(' '.join(['out', str(left), str(mid), str(right)]))
        if left < len(nums) and nums[left] == target:
            return left
        return -1

res = Solution().process([2, 2], 3)
print ('>>>>>>>>>>>>>>>')
print (res)

