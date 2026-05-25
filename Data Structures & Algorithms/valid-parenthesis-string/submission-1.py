from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        parStack = deque()
        starStack = deque()

        for i in range(len(s)):
            if s[i] == "(":
                parStack.append(i)
            elif s[i] == "*":
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
        
        return False if parStack else True
                
        