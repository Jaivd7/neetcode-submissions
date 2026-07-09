class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #3
        cols = len(matrix[0])
        low = 0
        high = (rows * cols) - 1
        # print(high)
        while (low<=high):
        # for i in range(4):
            mid = (low + high)//2
            mid_rows = (mid) // cols
            mid_cols = (mid) % cols
            mid_val = matrix[mid_rows][mid_cols]
            print(mid, mid_rows, mid_cols, "mid val", mid_val)
            if(target == mid_val):
                return True
            elif (target < mid_val):
                high = mid -1
            else:
                low = mid +1
            print("low", low, "high", high)
        return False
        