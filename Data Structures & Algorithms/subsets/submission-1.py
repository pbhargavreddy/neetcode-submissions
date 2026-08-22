class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        def recur(idx,path):
            if idx == N:
                res.append(path.copy())
                return
            #pick
            recur(idx+1,path+[nums[idx]])
            #Not pick
            recur(idx+1,path)
        recur(0,[])
        return res