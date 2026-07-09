class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList) #For O(1) lookup

        if endWord not in words or beginWord == endWord:
            return 0
        
        q = deque([(beginWord, 1)])
        visit = set(beginWord)

        while q:
            curr, curr_depth = q.popleft()

            for i in range(len(curr)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    nword = curr[:i] + c + curr[i+1:]

                    if nword == endWord:
                        return curr_depth + 1
                    
                    if nword in words and nword not in visit:
                        visit.add(nword)
                        q.append((nword,curr_depth + 1))
        return 0