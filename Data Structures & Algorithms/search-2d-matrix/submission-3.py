class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        m = len(matrix)
        n = len(matrix[0])
        while i<m:
            j = 0
            k = n - 1
            while j <= k:
                mid = (j + k)//2
                if matrix[i][mid] == target:
                    return True

                elif target > matrix[i][mid]:
                    j = mid+1

                elif target < matrix[i][mid]:
                    k = mid - 1
                
            i +=1

        return False

