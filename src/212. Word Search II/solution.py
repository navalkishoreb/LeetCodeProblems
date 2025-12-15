class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word: str):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or (r,c) in visit
            or board[r][c] not in node.children):
                return 

            visit.add((r,c))
            ch = board[r][c] 
            word += ch
            node = node.children[ch]
            if node.isWord:
                res.add(word)
         

            dfs(r -1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c -1, node, word)
            dfs(r, c + 1, node, word)
            
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

