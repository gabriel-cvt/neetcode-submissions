from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:    
        
        words = set(wordList)
        def buildNeigh(word, graph):
            graph[word] = []
            arrWord = list(word)
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    tmpArr = arrWord[:]
                    tmpArr[i] = chr(j)
                    tmp = "".join(tmpArr)
                    if tmp == word:
                        continue
                    if tmp in words:
                        graph[word].append(tmp)
        
        
        def bfs(graph, word, distance, parent):
            q = deque()
            distance[word] = 1
            q.append(word)

            while q:
                node = q.popleft()
                buildNeigh(node, graph)
                for nextWord in graph[node]:
                    if distance[nextWord] == float('inf'):
                        parent[nextWord] = node
                        distance[nextWord] = distance[node] + 1
                        q.append(nextWord)

        n = len(wordList) + 2
        parent = {word : -1 for word in wordList}
        parent[beginWord] = -1
        parent[endWord] = -1

        distance = {word: float('inf') for word in wordList}
        distance[beginWord] = float('inf')
        distance[endWord] = float('inf')

        bfs({}, beginWord, distance, parent)
        if distance[endWord] == float('inf'):
            return 0
        return distance[endWord]