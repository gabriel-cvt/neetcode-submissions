from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        
        visited = set()
        result = []
        def dfs(course, seen):
            nonlocal result
            if course in visited:
                return True
            
            if course in seen:
                return False
            
            seen.add(course)
            for next_course in graph.get(course, []):
                if not dfs(next_course, seen):
                    return False
            
            result.append(course)
            visited.add(course)
            seen.remove(course)
            return True

        seen = set()
        for i in range(numCourses):
            if not dfs(i, seen):
                return []

        return result        