class WordDictionary:
    class trie_node:
        def __init__(self):
            self.children = [None] * 26
            self.word = False
    
    def __init__(self):
        self.root = self.trie_node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = self.trie_node()
            curr = curr.children[ord(c) - ord('a')]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children:
                        if child == None:
                            continue
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if curr.children[ord(c) - ord('a')] == None:
                        return False
                    curr = curr.children[ord(c) - ord('a')]
            return curr.word
        
        return dfs(0, self.root)
