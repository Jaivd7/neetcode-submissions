class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        curr = []

        def isPalindrome(element):
            for i in range(len(element)):
                if element[i] != element[len(element) - i - 1]:
                    return False
            return True
        def dfs(i):
            #Base Case
            if i == len(s):
                out.append(curr[:])
                return
            
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    curr.append(s[i:j])
                    dfs(j)
                    curr.pop()
            


        dfs(0)
        #print(out)
        return out