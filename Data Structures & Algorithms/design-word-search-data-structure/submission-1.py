class TrieNode:

    def __init__(self):
        self.hmap = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.hmap.get(c):
                curr.hmap[c] = TrieNode()
            curr = curr.hmap[c]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(i, root):
            if i==len(word):
                return root.end
            
            if word[i] != '.':
                if not root.hmap.get(word[i]):
                    return False
                else:
                    return dfs(i+1, root.hmap[word[i]])
            else:
                flag = False
                for key, value in root.hmap.items():
                    if value:
                        flag = flag or dfs(i+1,value)
                return flag
        return dfs(0,curr)