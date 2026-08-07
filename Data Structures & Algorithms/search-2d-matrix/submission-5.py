class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        def matrixToLinear(row, col):
            return (row*numCols) + col
        
        def linearToMatrix(index):
            return ((index//numCols), (index%numCols))

        low, high = 0, (numRows*numCols) - 1

        while low <= high:
            mid = (low+high)//2
            mid_r, mid_c = linearToMatrix(mid)
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False