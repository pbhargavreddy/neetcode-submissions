class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = max(nums[:k])
        res = [maxi]
        for i in range(1,len(nums)-k+1):
            if nums[i+k-1]>res[-1]:
                res.append(nums[i+k-1])
            elif nums[i-1] == res[-1] and res[-1] not in nums[i:i+k]:
                res.append(max(nums[i:i+k]))
            else:
                res.append(res[-1])
            
        return res