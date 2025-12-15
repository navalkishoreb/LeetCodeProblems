class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store full word instead of isWord

    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = word


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None   # avoid duplicates

            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            board[r][c] = ch

            # prune trie
            if not nxt.children:
                node.children.pop(ch)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res

