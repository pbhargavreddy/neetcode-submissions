class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. Find pivot element. i.e starting point of sorted original array
        2. Then decide which half to search.
        """
        left = 0
        right = len(nums)-1
        while(left<right):
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        
        pivot = left
        # Check which side of pivot to search
        if nums[pivot] <=target <= nums[-1]:
            left = pivot
            right = len(nums) -1
        else:
            left = 0
            right = pivot-1

        # Normal binary search
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1