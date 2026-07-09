class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i,j):
            # if word1 is exhausted, insert all remaining of word2
            if i == len(word1):
                return len(word2) - j
            # if word2 is exhausted, delete all remaining of word1
            if j == len(word2):
                return len(word1) - i
            if (i,j) in dp:
                return dp[(i,j)]

            # If they match just continue
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
            else: # If they don't match
                rem = dfs(i+1,j) #Remove
                rep = dfs(i+1,j+1) #Replace
                ins = dfs(i, j+1) #Insert
                dp[(i,j)] = min(rem,rep,ins) + 1
            return dp[(i,j)]
        return dfs(0,0)