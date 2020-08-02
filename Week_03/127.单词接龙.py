#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not wordList or endWord not in wordList:
            return 0
        
        L = len(endWord)

        newWordList = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                newWordList[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = [(beginWord, 1)]
        visited = {beginWord: True}

        while queue:
            cur, step = queue.pop(0)

            for i in range(L):
                interm = cur[:i] + '*' + cur[i+1:]
                for tmp in newWordList[interm]:
                    if tmp == endWord:
                        return step + 1
                    if tmp not in visited:
                        queue.append((tmp, step+1))
                        visited[tmp] = True
                newWordList[interm] = []
        
        return 0


        
# @lc code=end

