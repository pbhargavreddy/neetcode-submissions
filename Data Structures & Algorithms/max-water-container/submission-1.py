class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l , r = 0,len(heights)-1
        while(l<r):
            area = (r-l)*min(heights[l],heights[r])
            maxi = max(area,maxi)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxi