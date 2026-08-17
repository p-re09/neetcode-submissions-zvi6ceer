class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        not_in_wordList = True
        for i in wordList:
            if endWord == i:
                not_in_wordList = False
        if not_in_wordList:
            return 0
        
        ans = 1
        q = collections.deque()
        q.append(beginWord)
        count = 0
        visit = set()


        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                for j in range(len(wordList)):
                    if j not in visit:
                        for num in range(len(wordList[j])):
                            if wordList[j][num] != node[num]:
                                count += 1
                        if count == 1:
                            if wordList[j] == endWord:
                                ans += 1
                                return ans
                            visit.add(j)
                            q.append(wordList[j])
                        count = 0
            ans += 1

        return 0



        