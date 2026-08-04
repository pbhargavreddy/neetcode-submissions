class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        # If either of n, m is 0 return middle element.
        if n==0:
            mid = m//2
            return nums2[mid] if m%2 ==1 else (nums2[mid]+nums2[mid-1])/2
        if m==0:
            mid = n//2
            return nums1[mid] if n%2 ==1 else (nums1[mid]+nums1[mid-1])/2
        # Find middle element or middle two elements
        i=j=0
        curr = 0
        for _ in range(((m+n)//2)+1):
            prev = curr
            if i<n and (j>=m or nums1[i]<nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j +=1
        return curr if (m+n)%2 == 1 else (prev+curr)/2