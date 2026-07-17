class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =  []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while(l<r):
                summ = nums[i]+nums[l]+nums[r]
                if summ == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1
                    
                elif summ>0:
                    r-=1
                else:
                    l +=1
        return res