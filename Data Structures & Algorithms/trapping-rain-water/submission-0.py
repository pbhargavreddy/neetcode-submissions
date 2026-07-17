class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        # l = 0
        n = len(height)
        # while(l<n and nums[l]>=nums[l+1]):
        #     l +=1
        # r = l+1
        # end = n-1
        # while(end>0 and nums[end]<=nums[end+1]):
        #     end -=1
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        
        right_max[-1] = height[-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        
        for i in range(n):
            curr= min(left_max[i],right_max[i])-height[i]
            if curr >0:
                water+=curr
        return water


