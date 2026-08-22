class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def recur(idx,path,curr_sum):
            if curr_sum== target:
                res.append(path.copy())
                return
            if curr_sum>target or idx>=len(nums):
                return
            
            for i in range(idx,len(nums)):
                recur(i,path+[nums[i]],curr_sum+nums[i])
        recur(0,[],0)
        return res