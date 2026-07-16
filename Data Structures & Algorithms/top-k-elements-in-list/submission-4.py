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
        # print(buckle)
        for i in range(len(buckle)-1,-1,-1):
            if buckle[i] :
                for num in buckle[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                
        # print(res)