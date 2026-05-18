from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        
        graph = {i : [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def bfs(node, graph):
            nonlocal result
            if node in visited:
                return
            
            q = deque()
            q.append(node)
            visited.add(node)

            while q:
                node = q.popleft()
                for neigh in graph[node]:
                    if neigh in visited:
                        continue
                    q.append(neigh)
                    visited.add(neigh)
            result += 1

        for i in range(n):
            bfs(i, graph)

        return result