class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        subset = []

        def dfs(curr):
            #Base Cases
            if len(subset) == k:
                out.append(subset.copy())
                return
            # Prune: no way to reach length k even if we take everything left
            remaining_needed = k - len(subset)
            remaining_available = n - curr + 1
            if remaining_available < remaining_needed:
                return
            
            #Include
            subset.append(curr)
            dfs(curr+1)
            subset.pop()

            #Do not include
            dfs(curr+1)
        dfs(1)
        return out