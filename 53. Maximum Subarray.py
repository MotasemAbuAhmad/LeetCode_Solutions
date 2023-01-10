from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sum_max = nums[0]
        sum_cur = nums[0]
        for i in range(1, len(nums)):
            if sum_cur >=0:
                if nums[i]>=0:
                    sum_cur += nums[i]
                else:
                    sum_max = max(sum_max, sum_cur)
                    sum_cur += nums[i]
            else:
                if nums[i]>=0:
                    sum_cur = nums[i]
                else:
                    sum_max = max(sum_max, sum_cur)
                    sum_cur = nums[i]
        return max(sum_max, sum_cur)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))