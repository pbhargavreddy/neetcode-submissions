class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(row):
            l = 0
            r = len(matrix[0])-1
            while(l<=r):
                mid = (r+l)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return False

        l = 0
        r = len(matrix)-1
        while(l<=r):
            mid = (r+l)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0] > target:
                if mid!= 0 and matrix[mid-1][0] < target:
                    return bs(mid-1)
                else:
                    r = mid-1
            elif matrix[mid][0] < target:
                if mid != len(matrix)-1 and matrix[mid+1][0] > target:
                    return bs(mid)
                else:
                    l = mid+1
        if r >= 0:
            return bs(r)
        return False
