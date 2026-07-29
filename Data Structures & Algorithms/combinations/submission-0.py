class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        subset = []

        def dfs(curr):
            #Base Cases
            if len(subset) == k:
                if subset not in out:
                    out.append(subset.copy())
                return
            if curr > n: #Too large a number
                return 
            
            #Include
            subset.append(curr)
            dfs(curr+1)
            subset.pop()

            #Do not include
            dfs(curr+1)
        dfs(1)
        return out