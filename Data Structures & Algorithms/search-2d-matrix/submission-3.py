class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = matrix
        numCols = len(nums[0])
        numRows = len(nums)
        low, high = 0, numCols*numRows-1

        while (low<=high):
            mid = (low+high)//2
            r = mid // numCols
            c = mid % numCols
            if(nums[r][c] == target):
                return True
            elif(nums[r][c] > target):
                high = mid - 1
            else:
                low = mid + 1
        return False
