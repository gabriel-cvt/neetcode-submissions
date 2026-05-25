from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        parStack = deque()
        starStack = deque()

        for i, ch in enumerate(s):
            if ch == "(":
                parStack.append(i)
            elif ch == "*":
                starStack.append(i)
            else:
                if parStack:
                    parStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        while parStack and starStack:
            par = parStack.pop()
            star = starStack.pop()
            if star < par:
                return False
        
        return not parStack
                
        