from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = []
        
        graph = {i : [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def bfs(node, graph, connected):
            if node in visited:
                return
            
            q = deque()
            q.append(node)
            seen = set()
            seen.add(node)
            visited.add(node)

            while q:
                node = q.popleft()
                for neigh in graph[node]:
                    if neigh in seen:
                        continue
                    seen.add(neigh)
                    connected.append(neigh)
                    q.append(neigh)
                    visited.add(neigh)
            result.append(connected)

        for i in range(n):
            bfs(i, graph, [])

        return len(result)