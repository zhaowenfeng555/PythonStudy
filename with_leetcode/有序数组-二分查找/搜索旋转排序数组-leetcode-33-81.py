# encoding: utf-8
# @author: fengr358
# @time: 2021/4/27 23:08
# @desc:

# @question: 旋转有序数组，查找给定值
# @answer：


# 找出mid，该索引为 mid =（left + right）/ 2，但是这样写有可能溢出，所以我们需要改进一下写成
#
# mid = left +（right - left）/ 2 或者 left + ((right - left ) >> 1) 两者作用是一样的，都是为了找到两指针的中
#
# 间索引，使用位运算的速度更快。那么此时的 mid = 0 + (8-0) / 2 = 4

class Solution:

    # 可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。
    # 拿示例来看，我们从 6 这个位置分开以后数组变成了 [4, 5, 6] 和 [7, 0, 1, 2] 两个部分，
    # 其中左边 [4, 5, 6] 这个部分的数组是有序的，其他也是如此。
    #
    # 这启示我们可以在常规二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
    # 并根据有序的那个部分确定我们该如何改变二分查找的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分：
    #
    # 如果 [l, mid - 1] 是有序数组，且 target 的大小满足 [nums[l],nums[mid])，
    # 则我们应该将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。

    # 如果 [mid, r] 是有序数组，且 target 的大小满足 (nums[mid+1],nums[r]]，
    # 则我们应该将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。
    def search_33(self, nums, target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # # 0 到中间的数，如果有序，则一定前半部分不包含旋转点
            # if nums[0] <= nums[mid]:
            #     if nums[0] <= target < nums[mid]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else:
            #     if nums[mid] < target <= nums[len(nums) - 1]:
            #         l = mid + 1
            #     else:
            #         r = mid - 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


    # 对于数组中有重复元素的情况，二分查找时可能会有 a[l]=a[mid]=a[r]，此时无法判断区间 [l,mid] 和区间 [mid+1,r] 哪个是有序的。
    #
    # 例如 nums=[3,1,2,3,3,3,3]，target=2，首次二分时无法判断区间 [0,3] 和区间 [4,6] 哪个是有序的。
    #
    # 对于这种情况，我们只能将当前二分区间的左边界加一，右边界减一，然后在新区间上继续二分查找。
    def search_81(self, nums, target: int) -> int:
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

print (Solution().search_33([4,5,6,7,0,1,2], 0))
print (Solution().search_81([4,4,5,6,7,0,0,1,2], 0))