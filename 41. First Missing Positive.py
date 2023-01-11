import sys
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # suppose p is the number of positive integers,then our missing is either p+1 or between 1 and p
        # p = sum(x > 0 for x in nums)
        # c = sum((x>0 and x<=p) for x in nums)
        p = 0
        # if c == p:
        # return p+1
        mini = sys.maxsize
        for i in range(len(nums)):
            if nums[i] > 0:
                mini = min(mini, nums[i])
                p += 1
            else:
                nums[i] = 0
        if p == 0:
            return 1
        if mini != 1:
            return 1
        uniq = 0
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] > p:
                if i < p:
                    nums[i] = 1
                else:
                    nums[i] = 0
        for i in range(len(nums)):
            marky = nums[abs(nums[i]) - 1]
            if nums[i] != 0 and marky > 0:
                uniq += 1
                nums[abs(nums[i]) - 1] = -abs(marky)
        if uniq >= p:
            return p + 1
        for i in range(uniq):
            if nums[i] > 0:
                return i + 1
        return uniq + 1


if __name__ == '__main__':
    nums = [1, 1, 1, 122, 2, 2, 2, 23,4,5,3]
    s = Solution()
    print(s.firstMissingPositive(nums))
