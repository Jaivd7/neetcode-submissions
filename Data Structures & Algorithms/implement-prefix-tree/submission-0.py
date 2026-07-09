class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            order = ord(c) - ord('a')
            if curr.children[order]:
                curr = curr.children[order]
            else:
                newnode = TrieNode()
                curr.children[order] = newnode
                curr = curr.children[order]
        curr.endOfWord = True    
        
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            order = ord(c) - ord('a')
            if curr.children[order]:
                curr = curr.children[order]
            else:
                return False
        if curr.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            order = ord(c) - ord('a')
            if curr.children[order]:
                curr = curr.children[order]
            else:
                return False
        return True
        
        