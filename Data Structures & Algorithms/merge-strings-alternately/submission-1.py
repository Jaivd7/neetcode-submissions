class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        result = []  # Use a list instead of a string. 
        # Python cannot simply append the characters in place. Instead, it has to allocate a brand new string in 
        # memory and copy all the characters from the old string s into the new one.
        while w1 < len(word1) and w2 < len(word2):
            result.append(word1[w1])
            result.append(word2[w2])
            w1 += 1
            w2 += 1
            
        # Append the remainder of whichever string is longer
        result.append(word1[w1:])
        result.append(word2[w2:])
        
        return "".join(result)  # O(N + M) join at the end