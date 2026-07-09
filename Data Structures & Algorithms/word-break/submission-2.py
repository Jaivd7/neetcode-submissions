class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp.append(True)
        for i in range(len(s)-1, -1, -1):
            for j in range(len(wordDict)):
                word = wordDict[j]
                if i+len(word)>len(s):
                    continue
                else:
                    if s[i:i+len(word)] == word:
                        #print(i, word, dp)
                        if not dp[i]:
                            dp[i] = dp[i+len(word)]
        #print("Final ", dp)
        return dp[0]
                