class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.ends = True

    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        if temp.ends == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)