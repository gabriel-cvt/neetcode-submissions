from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        
        seen = set()
        visited = set()
        def dfs(course, seen):
            if course in seen:
                return False
            
            if course in visited:
                return True
            
            seen.add(course)
            for req in graph.get(course, []):
                if not dfs(req, seen):
                    return False
            visited.add(course)
            seen.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i, seen):
                return False
        return True
        