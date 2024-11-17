"""
- Title: Implement Trie (Prefix Tree)
- Difficulty: Medium
- Question ID: 208
- Status: Solved
- Topic Names: Hash Table, String, Design, Trie
- URL: https://leetcode.com/problems/implement-trie-prefix-tree
"""


class TrieNode:

    def __init__(self):

        self.children = {}
        self.eow = False # end of the word

class Trie:

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for char in word:

            # check if a certain character exist at a node or not
            if curr.children.get(char) == None:

                curr.children[char] = TrieNode()
            
            curr = curr.children[char] 
        curr.eow = True

    def search(self, word: str) -> bool:
        
        curr = self.root
        for char in word:

            # check if a node exists or not
            if curr.children.get(char) != None:

                # if the node exist update and check for next character
                curr = curr.children[char]
            else:
                return False
        
        if curr.eow == True:

            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root
        for char in prefix:

            # check if a node exists or not
            if curr.children.get(char) != None:

                # if the node exist update and check for next character
                curr = curr.children[char]
            else:
                return False
                
        return True
        



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
