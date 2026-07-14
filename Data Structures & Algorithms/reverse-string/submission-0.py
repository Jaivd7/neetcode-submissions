class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i,j,nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        st, l = 0, (len(s)-1)
        while st<l:
            swap(st,l,s)
            st +=1 
            l -=1
        
