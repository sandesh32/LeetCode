class TrieNode:
    
    def __init__(self):
        self.children = [None for i in range(26)]
        self.ends = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        temp = self.root
        for c in word:
            if temp.children[ord(c)-ord('a')]==None:
                temp.children[ord(c)-ord('a')] = TrieNode()
            temp = temp.children[ord(c)-ord('a')]
        temp.ends = True

    def search(self, word: str) -> bool:
        
        temp = self.root
        for c in word:
            if temp.children[ord(c)-ord('a')]:
                temp = temp.children[ord(c)-ord('a')]
            else:
                return False
        return temp.ends

    def startsWith(self, prefix: str) -> bool:
        
        temp = self.root
        for c in prefix:
            if temp.children[ord(c)-ord('a')]:
                temp = temp.children[ord(c)-ord('a')]
            else:
                return False
        return True
        