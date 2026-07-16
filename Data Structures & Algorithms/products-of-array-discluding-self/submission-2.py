class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        s = 1
        s0 = 1
        for i in range(len(nums)):
            s *= nums[i]
            if nums[i] ==0:
                continue
            s0 *=nums[i]
        output = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] ==0:
                output[i] = s0
            else:
                output[i] = int(s / nums[i])
        return output

        # res[i] = res[i-1]/nums[i-1] * nums[i]