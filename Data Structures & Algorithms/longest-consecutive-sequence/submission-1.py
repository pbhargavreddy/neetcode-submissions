from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seen = [False]*len(nums)
        if not nums:
            return 0
        maxi = 1
        for i in range(len(nums)):
            if nums[i]-1 not in nums:
                c = 1
                x = nums[i]+1
                while(x in nums):
                    c += 1
                    x +=1
                maxi = max(c,maxi)
        return maxi