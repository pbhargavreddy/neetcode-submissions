class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recur(idx,path):
            res.append(path.copy())
            for i in range(idx,len(nums)):
                recur(i+1,path+[nums[i]])
        recur(0,[])
        return res