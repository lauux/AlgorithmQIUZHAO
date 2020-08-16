#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:

    def __init__(self) -> None:
        self.res = set()
        self.lookup = dict()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board or not board[0]:
            return []

        m, n = len(board), len(board[0])
        visited = set()
        self.createTrieTree(words)
        for i in range(m):
            for j in range(n):
                self.backtrack('', board, i, j, self.lookup, visited)

        return list(self.res)

    def createTrieTree(self, words: List[str]) -> None:
        for word in words:
            tree = self.lookup
            for char in word:
                if char not in tree:
                    tree[char] = {}
                tree = tree[char]
            tree['#'] = '#'
    
    def backtrack(self, chars: str, board: List[List[str]], row: int, col: int, tree: dict, visited: set) -> None:
        if '#' in tree:
            self.res.add(chars)

        m, n = len(board), len(board[0])
        if 0 <= row < m and 0 <= col < n:
            char = board[row][col]
            if char not in tree:
                return

            visited.add((row, col))
            for r, c in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
                if (r, c) not in visited:
                    self.backtrack(chars + char, board, r, c, tree[char], visited)
            visited.remove((row, col))
# @lc code=end

