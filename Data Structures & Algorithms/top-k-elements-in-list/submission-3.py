class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        # print(freq)
        buckle = [[] for _ in range(len(nums)+1)]
        for key , value in freq.items():
            buckle[value].append(key)
        print(buckle)
        for i in range(len(buckle)-1,-1,-1):
            if buckle[i] and k>0:
                path = [buckle[i][j] for j in range(len(buckle[i]))]
                res += path
                k -=len(buckle[i])
            if k==0:
                break
        # print(res)
        return res