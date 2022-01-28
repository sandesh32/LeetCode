class WordDictionary:

    def __init__(self):
        self.dict={}

    def addWord(self, word: str) -> None:
        if len(word) in self.dict:
            self.dict[len(word)].append(word)
            return
        self.dict[len(word)]=[word]

    def search(self, word: str) -> bool:
         if len(word) not in self.dict:
                return False
         if "." not in word:
            return word in self.dict[len(word)]
         for i in self.dict[len(word)]:
                count=len(word)
                for j in range(len(word)):
                    if word[j]!="." and word[j]!=i[j]:
                        count-=1
                        break
                if count==len(word):
                    return True
         return False
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)