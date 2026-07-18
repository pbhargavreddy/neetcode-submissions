class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        k_min = float('inf')
        while(l<=r):
            k = (r+l) //2
            curr = 0
            for pile in piles:
                curr += math.ceil(pile/k)
            if curr <= h:
                k_min = min(k,k_min)
                r = k-1
            else:
                l = k+1
        return k_min

